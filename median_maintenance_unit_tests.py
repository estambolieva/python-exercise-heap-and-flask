import unittest
from median_maintenance import get_median

class TestStringMethods(unittest.TestCase):

    def test_sequence1(self):
        self.assertEqual(get_median([1, 5, 8, 9, 20]), 8)

    def test_sequence2(self):
        self.assertEqual(get_median([1, 2, 34, 23, 20, 19, 18, 50, 6, 13, 12]), 18)

    def test_sequence3(self):
        self.assertEqual(get_median([706, 902, 122, 372, 155, 929, 4, 58, 66, 971, 588, 772, 711, 392, 280, 109, 755, 51, 378, 490, 76, 25, 736, 771, 563, 78]), 378)

    def test_sequence4(self):
        self.assertEqual(get_median([39, 86, 26, 75, 63, 80, 11, 7, 53, 3, 74, 20, 27, 58, 36, 49, 69]), 49)

    def test_sequence5(self):
        self.assertEqual(get_median([10,9,8,7,6,5,4,3,2,1]), 5)

    def test_sequence6(self):
        self.assertEqual(get_median([1,2,3,4,5,6,7,8,9,10,11]), 6)

    def test_sequence7(self):
        self.assertEqual(get_median([1,2,34,23,20,19,18,50,6]), 19)

    def test_sequence8(self):
        self.assertEqual(get_median([20,9,19,11,14,8,15,23,6,50,32,22]), 15)

    def test_sequence9(self):
        self.assertEqual(get_median([1, 2, 3, 5]), 2)
    
    def test_sequence10(self):
        self.assertEqual(get_median([12, 56, 89, 23]), 23)

    def test_sequence11(self):
        self.assertEqual(get_median([1, 2, 3, 5]), 2)

    def test_sequence12(self):
   		self.assertEqual(get_median([4, 6, 1, 8, 3, 6, 9, 10]), 6)

    def test_sequence13(self):
        self.assertEqual(get_median([1, 2, 5, 13, 89, 468, 69]), 13)

    def test_sequence14(self):
        self.assertEqual(get_median([1, 5, 6, 89, 468, 69]), 6)

if __name__ == '__main__':
    unittest.main()