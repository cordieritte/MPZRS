import unittest
from comp import Comp

class TestComp(unittest.TestCase):
    def test_no_ping(self):
        comp = Comp()
        answer = comp.iface().ping("1.2.3.4")
        self.assertEqual(answer, "No network")

if __name__ == '__main__':
    unittest.main()
