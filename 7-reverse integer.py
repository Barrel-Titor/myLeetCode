"""
https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x: int) -> int:
        signed = 1 if x >= 0 else -1
        positive_part = x * signed
        digits_reversed = []
        remained = positive_part
        while remained > 0:
            digits_reversed.append(remained % 10)
            remained //= 10

        result = 0
        for d in digits_reversed:
            result *= 10
            result += d
        result *= signed

        if -2**31 <= result <= 2**31-1:
            return result
        else:
            return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(583))
