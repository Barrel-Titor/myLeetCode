"""
https://leetcode.com/problems/implement-strstr/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # 算法第 4 版
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            for j in range(n):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1


class KMPSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
