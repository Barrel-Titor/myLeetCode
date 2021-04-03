"""
https://leetcode.com/problems/remove-element/
"""
from typing import List


class Solution:
    # Wrong answer
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == val:
                # swap nums[i] and nums[j]
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                j -= 1
            else:
                i += 1
        return i + 1


class OfficalSolution1:
    """
    When nums[j] equals to the given value, skip this element by incrementing j.
    As long as nums[j] != val, we copy nums[j] to nums[i] and increment both indexes at the same time.
    Repeat the process until j reaches the end of the array and the new length is i.
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


class OfficalSolution2:
    """
    When we encounter nums[i] = val, we can swap the current element out with the last element and dispose the last one.
    This essentially reduces the array's size by 1.
    Note that the last element that was swapped in could be the value you want to remove itself.
    But don't worry, in the next iteration we will still check this element.
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            if nums[i] == val:
                nums[i] = nums[j - 1]
                j -= 1
            else:
                i += 1
        return j
