"""Computer network"""

class Network:
    """Network represents net"""
    
    
    def __init__(self):
        self._hosts = {}
        
    def add_host(self, comp, address):
        """Add host to net"""
        self._hosts[address] = comp
        comp.iface().setup(self, address)
    
    def ping(self, src, dst):
        """Ping sends ping to host"""
        if dst in self._hosts:
            return f"ping from {src} to {dst}"
        
        return "Unknown host"
    
    def resolve(self, dns_address, name):
        try:
            return self._hosts[dns_address].resolve(name)
        except KeyError:
            return None
        