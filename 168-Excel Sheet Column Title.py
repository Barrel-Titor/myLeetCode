"""
https://leetcode.com/problems/excel-sheet-column-title/
"""


class Solution:
    """
    https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation

    we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4

    But how to get the column title from the number? We can't simply use the n%26 method because:

    ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26

    We can use (n-1)%26 instead, then we get a number range from 0 to 25.
    """
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []
        num = columnNumber
        while num:
            result.append(capitals[(num - 1) % 26])
            num = (num - 1) // 26
        result.reverse()
        return ''.join(result)
