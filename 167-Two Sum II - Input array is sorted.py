"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in table.keys():
                return [table[complement], i + 1]
            else:
                table[num] = i + 1


class OldCodingFarmerSolution:
    """https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search).
    two pointer

    Two pointers: O(n) time and O(1) space
    Dictionary: O(n) time and O(n) space
    Binary search: O(nlogn) time and O(1) space
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            elif s > target:
                r -= 1