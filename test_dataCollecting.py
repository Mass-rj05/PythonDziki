import unittest
import dataCollecting

class TestDataCollecting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def test_appendingAreasName(self):
        self.assertIsNotNone(self)

class TestValidateData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def test_validateData(self):
        self.assertIsNotNone(dataCollecting.validateLinks(self))

if __name__ == '__main__':
    unittest.main()