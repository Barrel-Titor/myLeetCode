from typing import List, Optional

#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = self.findPalindrome(s, i, i)
            even = self.findPalindrome(s, i, i + 1)
            res = max(res, odd, even, key=len)
        return res

    def findPalindrome(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]


# @lc code=end
