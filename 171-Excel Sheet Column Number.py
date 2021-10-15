"""
https://leetcode.com/problems/excel-sheet-column-number/
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            n = ord(ch) - ord('A') + 1
            result *= 26
            result += n
        return result