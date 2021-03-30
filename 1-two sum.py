"""
https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in table.keys():
                return [table[complement], i]
            else:
                table[num] = i