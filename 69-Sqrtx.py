"""
https://leetcode.com/problems/sqrtx/
"""
import unittest


class Solution:
    def mySqrt(self, x: int) -> int:
        # s = sr * sr
        s = sr = 0
        while s <= x:
            if s == x:
                return sr
            else:
                sr += 1
                s = sr * sr
        return sr - 1


class BinarySearch1:
    """
    https://leetcode.com/problems/sqrtx/discuss/25047/A-Binary-Search-Solution
    """

    def mySqrt(self, x: int) -> int:
        # if x == 0:
        #     return 0
        left, right = 1, x
        while True:
            mid = left + (right - left) // 2  # avoid overflow
            if mid > x // mid:
                right = mid - 1
            elif (mid + 1) > x // (mid + 1):
                return mid
            else:
                left = mid + 1


class BinarySearch2:
    """
    Near the very end, closest step, before while loop, left = mid = right.
    In while, If mid < sqrt(x), left = mid + 1 executed, right pointer is not moving, and right is the answer.
    If while, If mid > sqrt(x), right = mid - 1 executed, right pointer shifts left 1, closest to sqrt(x),
    right is also the answer.
    """
    def mySqrt(self, x: int) -> int:
        # if x == 0:
        #     return 0
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2  # avoid overflow
            if mid == x // mid:
                return mid
            elif mid < x // mid:
                left = mid + 1
            else:
                right = mid - 1
        return right


class NewtonMethod:
    """
    https://leetcode.com/problems/sqrtx/discuss/25057/3-4-short-lines-Integer-Newton-Every-Language
    Explanation:
    https://leetcode.com/problems/sqrtx/discuss/25057/3-4-short-lines-Integer-Newton-Every-Language/24092
    Integer square root problem:
    https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division
    """

    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # self.sol = Solution()
        # self.sol = BinarySearch1()
        self.sol = BinarySearch2()

    def test_eg1(self):
        self.assertEqual(2, self.sol.mySqrt(4))

    def test_eg2(self):
        self.assertEqual(2, self.sol.mySqrt(8))


if __name__ == '__main__':
    unittest.main()
