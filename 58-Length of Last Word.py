"""
https://leetcode.com/problems/length-of-last-word/
"""
import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        # count trailing spaces
        for k in range(len(s)):
            if s[k] != ' ':
                break
        else:
            return 0

        for i in range(k, len(s)):
            if s[i] == ' ':
                return i - k
        return i - k + 1


class OneLineSolution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0 if len(s.split()) == 0 else len(s.split()[-1])


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_eg1(self):
        self.assertEqual(5, self.sol.lengthOfLastWord("Hello World"))

    def test_eg2(self):
        self.assertEqual(0, self.sol.lengthOfLastWord(" "))

    def test_wrong1(self):
        self.assertEqual(1, self.sol.lengthOfLastWord("a"))

    def test_wrong2(self):
        self.assertEqual(5, self.sol.lengthOfLastWord("World"))

    def test_wrong3(self):
        # fuck you testcase
        self.assertEqual(1, self.sol.lengthOfLastWord("a "))


if __name__ == '__main__':
    unittest.main()
