"""DNS prototype"""


class Record:
    """Single DNS record"""

    def __init__(self, name, addr):
        self._name = name
        self._address = addr

    def get_name(self):
        """Return name of record"""
        return self._name

    def get_address(self):
        """Return address of record"""
        return self._address


class DnsDb:
    """DNS database"""

    def __init__(self):
        self._records = {}
        self._addresses = {}

    def num_records(self):
        """Return number of records"""
        return len(self._records)

    def add_record(self, record):
        """Add record"""
        self._check_record(record)
        self._records[record.get_name()] = record

    def resolve(self, name):
        """Return IP address by name"""
        try:
            return self._records[name].get_address()
        except KeyError:
            return None

    def _check_record(self, record):
        if record.get_address() in self._addresses:
            raise ValueError("Duplicated address")
        self._addresses[record.get_address()] = True
