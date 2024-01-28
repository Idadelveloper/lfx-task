import unittest
import main

class TestFunc(unittest.TestCase):

    def test_returnIntegers(self):
        self.assertEqual(main.returnIntegers([2, 5, 20, 10]), [5])
        self.assertEqual(main.returnIntegers([10, 2, 9, 3, 0, 1, 19, 8, 0, 67, 12, 15]), [2, 1, 8, 15])
        self.assertEqual(main.returnIntegers(["a", "5"]), [])
        

if __name__ == '__main__':
    unittest.main()