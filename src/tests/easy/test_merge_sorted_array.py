# src/tests/easy/test_merge_sorted_array.py

import unittest
from src.problems.easy.merge_sorted_array import Solution

class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_merge_case_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_merge_case_2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_merge_case_3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_merge_case_4(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_merge_case_5(self):
        nums1 = [2, 0]
        m = 1
        nums2 = [1]
        n = 1
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2])

    def test_merge_case_6(self):
        nums1 = [0, 0, 0]
        m = 0
        nums2 = [1, 2, 3]
        n = 3
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3])

    def test_merge_case_7(self):
        nums1 = [1, 0, 0, 0, 0]
        m = 1
        nums2 = [2, 3, 4, 5]
        n = 4
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5])

    def test_merge_case_8(self):
        nums1 = [2, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [1, 1, 1]
        n = 3
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 1, 1, 2, 2, 3])

    def test_merge_case_9(self):
        nums1 = [1, 2, 2, 0, 0, 0]
        m = 3
        nums2 = [2, 2, 2]
        n = 3
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 2, 2, 2])

    def test_merge_case_10(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [4, 5, 6]
        n = 3
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main()
