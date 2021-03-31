"""
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for ch in s:
            if ch in left:
                stack.append(ch)
            elif ch in right:
                if not stack:
                    return False

                i = right.index(ch)
                last = stack.pop()
                if last != left[i]:
                    return False

        return True if not stack else False


class gangarSolution:
    def isValid(self, s):
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("(]"))
    print(sol.isValid("([)]"))
    print(sol.isValid("{[]}"))
    print(sol.isValid("["))
    print(sol.isValid("]"))
