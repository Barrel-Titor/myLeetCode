"""
https://leetcode.com/problems/add-binary/
"""
import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        a = a[::-1]
        b = b[::-1]
        carry_bit = 0
        for i, (ch1, ch2) in enumerate(zip(a, b)):
            d1, d2 = int(ch1), int(ch2)
            tmp = d1 + d2 + carry_bit
            result.append(str(tmp % 2))
            carry_bit = tmp // 2

        remained = a[i + 1:] if len(a) > len(b) else b[i + 1:]
        for ch in remained:
            tmp = int(ch) + carry_bit
            result.append(str(tmp % 2))
            carry_bit = tmp // 2

        if carry_bit:
            result.append(str(carry_bit))
        return ''.join(result[::-1])


class lx223Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            tmp = carry
            if i >= 0:
                tmp += int(a[i])
                i -= 1
            if j >= 0:
                tmp += int(b[j])
                j -= 1
            result.append(str(tmp % 2))
            carry = tmp // 2

        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_eg1(self):
        self.assertEqual("100", self.sol.addBinary(**dict(a="11", b="1")))

    def test_eg2(self):
        self.assertEqual("10101", self.sol.addBinary(**dict(a="1010", b="1011")))

    def test_wrong(self):
        self.assertEqual("0", self.sol.addBinary(**dict(a="0", b="0")))


if __name__ == '__main__':
    unittest.main()
