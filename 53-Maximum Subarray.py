"""
https://leetcode.com/problems/maximum-subarray/
"""
import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = prev_sum = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            prev_sum = max(n, prev_sum + n)
            max_sum = max(max_sum, prev_sum)
        return max_sum


class MyTestCase(unittest.TestCase):
    def test_eg1(self):
        sol = Solution()
        self.assertEqual(6, sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_eg2(self):
        sol = Solution()
        self.assertEqual(1, sol.maxSubArray([1]))

    def test_eg3(self):
        sol = Solution()
        self.assertEqual(23, sol.maxSubArray([5, 4, -1, 7, 8]))

    def test_wrong1(self):
        sol = Solution()
        self.assertEqual(-1, sol.maxSubArray([-1]))

    def test_wrong2(self):
        sol = Solution()
        self.assertEqual(-2, sol.maxSubArray([-2, -3]))


if __name__ == '__main__':
    unittest.main()
