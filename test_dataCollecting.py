import unittest
import dataCollecting
import pandas as pd


class TestValidateData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def test_validateData(self):
        self.assertIsNot(dataCollecting.validateLinks(['https://www.skiresort.info/ski-resort/szczyrk-mountain-resort/test-result/size/','https://www.skiresort.info/ski-resort/szczyrk-mountain-resort/test-result/size/']), [])


    def test_makeDF(self):
        self.assertIsNot(dataCollecting.makeDF([['36.6', '733', '9'], ['18.3', '230', '19'], ['4', '261', '2']], ['Routes total', 'Elevation difference', 'Lifts total']), [])


if __name__ == '__main__':
    unittest.main()