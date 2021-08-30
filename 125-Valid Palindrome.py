"""
https://leetcode.com/problems/valid-palindrome/
"""


class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([ch for ch in s if ch.isalnum()])
        return s == s[::-1]


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([ch for ch in s if ch.isalnum()])
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    sol = Solution2()
    testcase1 = "A man, a plan, a canal: Panama"
    testcase2 = "race a car"
    testcase3 = "0P"
    testcase4 = "!!!"
    print(sol.isPalindrome(testcase1))
    print(sol.isPalindrome(testcase2))
    print(sol.isPalindrome(testcase3))
    print(sol.isPalindrome(testcase4))