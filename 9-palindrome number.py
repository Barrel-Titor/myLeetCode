"""
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = []

        remained = x
        while remained > 0:
            digits.append(remained % 10)
            remained //= 10

        remained = x
        for d in digits[::-1]:
            if remained % 10 != d:
                return False
            remained //= 10

        return True


class OfficialSolution:
    def isPalindrome(self, x: int) -> bool:
        # // Special cases:
        # // As discussed above, when x < 0, x is not a palindrome.
        # // Also if the last digit of the number is 0, in order to be a palindrome,
        # // the first digit of the number also needs to be 0.
        # // Only 0 satisfy this property.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted *= 10
            reverted += (x % 10)
            x //= 10

        # // When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        # // For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        # // since the middle digit doesn't matter in palindrome(it will always equal to itself),
        # we can simply get rid of it.
        return x == reverted or x == reverted // 10
