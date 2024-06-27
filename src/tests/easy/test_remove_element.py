# src/tests/easy/test_remove_element.py

import unittest
from src.problems.easy.remove_element import Solution

class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_removeElement_case_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, 2)
        self.assertEqual(sorted(nums[:k]), [2, 2])

    def test_removeElement_case_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [0, 0, 1, 3, 4])

    def test_removeElement_case_3(self):
        nums = []
        val = 1
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums, [])

    def test_removeElement_case_4(self):
        nums = [1, 1, 1, 1, 1]
        val = 1
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

    def test_removeElement_case_5(self):
        nums = [4, 5, 6, 7, 8]
        val = 3
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [4, 5, 6, 7, 8])

    def test_removeElement_case_6(self):
        nums = [1, 2, 3, 4, 5]
        val = 5
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, 4)
        self.assertEqual(sorted(nums[:k]), [1, 2, 3, 4])

    def test_removeElement_case_7(self):
        nums = [2, 2, 2, 2, 2]
        val = 2
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

    def test_removeElement_case_8(self):
        nums = [3, 3, 3, 3, 3, 3]
        val = 3
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

    def test_removeElement_case_9(self):
        nums = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        val = 1
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, 6)
        self.assertEqual(sorted(nums[:k]), [2, 2, 2, 3, 3, 3])

    def test_removeElement_case_10(self):
        nums = [2, 4, 6, 8, 10]
        val = 7
        k = self.sol.removeElement(nums, val)
        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [2, 4, 6, 8, 10])

if __name__ == "__main__":
    unittest.main()
