# src/problems/easy/merge_sorted_array.py

# 88. Merge Sorted Array 
# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """     
        del(nums1[m: (m + n)])              
        nums1 += nums2
        nums1.sort()
