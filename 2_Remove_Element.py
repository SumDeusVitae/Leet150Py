"""
27. Remove Element
Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place.
The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
        The remaining elements of nums are not important as well as the size of nums.
    Return k.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j: int = 0
        k: int = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
            else:
                j +=1
        if j > 0: del nums[-j:]
        return k