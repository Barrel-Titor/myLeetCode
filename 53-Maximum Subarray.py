"""
https://leetcode.com/problems/maximum-subarray/
"""
import math
import unittest
from typing import List


class Solution:
    """
    https://mp.weixin.qq.com/s/nrULqCsRsrPKi3Y-nUfnqg
    定义 dp 数组的含义：
    以 nums[i] 为结尾的「最大子数组和」为 dp[i]
    """
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, prev_sum = -math.inf, 0
        for n in nums:
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
