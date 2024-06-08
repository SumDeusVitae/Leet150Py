"""
169. Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # MOORE VOTING ALGORITHM
        counter: int = 0
        condidate: int = 0

        for num in nums:
            if counter == 0:
                condidate = num
            if num == condidate:
                counter += 1
            else:
                counter -= 1
            # print(condidate)
        return condidate