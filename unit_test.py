import csv_parser
import unittest
class test_csv_parser(unittest.TestCase):
    def test_load_func(self):
        x=csv_parser.load("House_pred.csv")
        pass
    def test_count_func(self):
        x=csv_parser.count()
        pass
if __name__=='__name__':
    unittest.main()

