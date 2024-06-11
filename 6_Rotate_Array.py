"""
189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i: int = 0
        while i < k:
            nums.insert(0,nums.pop(-1))
            i+=1
        