class NetworkInterface:
    """Network interface"""

    def __init__(self):
        self.net = None
        self.address = None
        self.dns = None

    def setup(self, net, addr):
        """Set net and address to interface"""
        self.net = net
        self.address = addr

    def set_dns_server(self, addr):
        """Set DNS server"""
        self.dns = addr

    def ping(self, addr):
        """Send ping to address"""
        if not self.net:
            return "No network"
        return self.net.ping(self.address, addr)

    def resolve(self, name):
        """Resolve name"""
        if not self.net:
            return None
        return self.net.resolve(self.dns, name)


class Comp:
    """Computer"""

    def __init__(self):
        self._iface = NetworkInterface()
        self._local_db = None

    def iface(self):
        """Return network interface"""
        return self._iface

    def resolve(self, name):
        """Resolve name"""
        if self._local_db:
            addr = self._local_db.resolve(name)
            if addr:
                return addr

        return self._iface.resolve(name)

    def set_dns_db(self, db):
        """Set DNS db"""
        self._local_db = db
