import unittest
import main

class TestFunc(unittest.TestCase):

    def test_returnIntegers(self):
        with self.assertRaises(Exception) as context:
            main.returnIntegers([2, 5, 20, 10])

        self.assertTrue('The length of the array([2, 5, 20, 10]) is not a multiple of 10' in str(context.exception))
        self.assertEqual(main.returnIntegers([10, 2, 9, 3, 0, 1, 19, 8, 0, 67]), [2, 1, 8])
        self.assertEqual(main.returnIntegers(["2", "5", "17", "10", "0", 19, "3", "7", "20", "80"]), [5, 19, 7])
        

if __name__ == '__main__':
    unittest.main()