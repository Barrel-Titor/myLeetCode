"""
https://leetcode.com/problems/plus-one/
"""
import unittest
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = digits[::-1]
        carry_bit = 1
        for i in range(len(result)):
            result[i] += carry_bit
            if result[i] < 10:
                carry_bit = 0
            else:
                carry_bit = 1
                result[i] = 0
        if carry_bit:
            result.append(1)
        return result[::-1]


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_eg1(self):
        self.assertEqual([1, 2, 4], self.sol.plusOne([1, 2, 3]))

    def test_eg2(self):
        self.assertEqual([4, 3, 2, 2], self.sol.plusOne([4, 3, 2, 1]))

    def test_eg3(self):
        self.assertEqual([1], self.sol.plusOne([0]))

    def test_eg4(self):
        self.assertEqual([1, 0, 0], self.sol.plusOne([9, 9]))


if __name__ == '__main__':
    unittest.main()
