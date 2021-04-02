"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 0
        length = len(nums)
        while i < length:
            if nums[i] == nums[j]:
                del nums[i]
                length -= 1
            else:
                j = i
                i += 1
        return length


class OfficialSolution:
    """
    i is the slow-runner while j is the fast-runner.
    As long as nums[i] = nums[j], we increment j to skip the duplicate.
    When we encounter nums[i] != nums[j], the duplicate run has ended so we must copy its value to nums[i + 1].
    i is then incremented and we repeat the same process again until j reaches the end of array.
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
