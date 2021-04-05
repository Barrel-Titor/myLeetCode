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
    """
    https://leetcode.com/problems/implement-strstr/discuss/13237/Java-and-Python-solution-using-KMP-with-O(m-%2B-n)-time-complexity
    The time complexity for this solution should be O(m + n).
    First of all, we generate the "next" array to show any possible duplicates of prefix and postfix within needle.
    Then we go through haystack.
    Every time we see a bad match, move j to next[j] and keep i in current position;
    otherwise, move both of them to next position.
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # generate next array, need O(n) time
        i, j, m, n = -1, 0, len(haystack), len(needle)
        next = [-1] * n
        while j < n - 1:
            # needle[k] stands for prefix, needle[j] stands for postfix
            if i == -1 or needle[i] == needle[j]:
                i, j = i + 1, j + 1
                next[j] = i
            else:
                i = next[i]
            print(i, j, next[i], next[j])

        # check through the haystack using next, need O(m) time
        i = j = 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = next[j]
        if j == n:
            return i - j
        return -1
