import unittest
from main import to_upper
 
class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = 'abhay'
        upper_name = to_upper(name) 
        self.assertEqual(upper_name, "abhay")

if __name__	== ' main ': 
    unittest.main()
