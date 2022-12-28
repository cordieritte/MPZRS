from db import Database


class System:
    """System with replication."""

    def __init__(self, repls_num=1):
        if repls_num < 1:
            raise ValueError("repls_num must be positive")

        self._main = Database()
        self._repls = []
        for _ in range(repls_num):
            self._repls.append(Database())

        self._stats = {
            "main": 0,
            "repl": [],
        }

        for _ in range(repls_num):
            self._stats["repl"].append(0)

        self._ind = 0

    def get_main(self):
        """Return main DB."""
        return self._main

    def get_repl(self, ind=0):
        """Return replicated DB."""
        return self._ind[ind]

    def sync(self):
        """Synchronize system."""
        for repl in self._repls:
            _sync(self._main, repl)

    def add_record(self, rec):
        """Add record to database."""
        return self._main.add_record(rec)

    def get_record(self, record_id):
        """Get record by ID."""
        rec = self._repls[self._ind].get_record(record_id)
        self._stats["repl"][self._ind] += 1
        self._update_ind()
        if rec:
            return rec
        return self._main.get_record(record_id)

    def get_all(self):
        """Return all records."""
        res = self._repls[self._ind].get_all()
        self._stats["repl"][self._ind] += 1
        self._update_ind()
        return res

    def stats(self):
        """Return statistics of readings."""
        return self._stats

    def _update_ind(self):
        self._ind = (self._ind + 1) % len(self._repls)


def _sync(src, dst):
    records = src.get_all()
    for rec_id, rec in records.items():
        if not dst.get_record(rec_id):
            dst.add_record(rec)
