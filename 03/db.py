class Database:
    """Database prototype."""

    def __init__(self):
        self._records = {}

    def records_num(self):
        return len(self._records)

    def add_record(self, record):
        if record.get_id() in self._records:
            raise ValueError("Duplicated ID")

        self._records[record.get_id()] = record

    def get_record(self, record_id):
        try:
            return self._records[record_id]
        except KeyError:
            return None

    def get_all(self):
        """Return all records."""
        return self._records
