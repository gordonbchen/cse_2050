# See assignment for class attributes.
# Remember to include docstrings.
# Start with unittests

class LocalRecord:
    def __init__(self, pos, max=None, min=None, precision = 0): pass

    def add_report(self, temp): pass

    def __eq__(self, other): pass

    def __hash__(self): pass

    def __repr__(self):
        return f"Record(pos={self.pos}, max={self.max}, min={self.min}"

class RecordsMap:
    def __init__(self): pass

    def __len__(self): pass

    def add_report(self, pos, temp): pass

    def __getitem__(self, pos): pass
  
    def __contains__(self, pos): pass

    def _rehash(self, m_new): pass