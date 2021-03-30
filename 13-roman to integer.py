"""
https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            '': 0,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0

        prev = ''
        for ch in s[::-1]:
            if table[ch] >= table[prev]:
                result += table[ch]
            else:
                result -= table[ch]
            prev = ch

        return result