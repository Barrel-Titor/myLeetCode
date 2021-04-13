"""
https://leetcode.com/problems/climbing-stairs/
"""
import unittest


class Solution:
    def __init__(self):
        self.table = {}

    def climbStairs(self, n: int) -> int:
        if not self.table.get(n):
            if n == 1 or n == 2:
                self.table[n] = n
            else:
                self.table[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.table[n]


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_eg1(self):
        self.assertEqual(2, self.sol.climbStairs(2))

    def test_eg2(self):
        self.assertEqual(3, self.sol.climbStairs(3))


if __name__ == '__main__':
    unittest.main()
