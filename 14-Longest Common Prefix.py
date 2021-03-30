"""
https://leetcode.com/problems/longest-common-prefix/

Further Thoughts:
https://leetcode.com/problems/implement-trie-prefix-tree/solution/
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        elif len(strs) >= 3:
            LCP_2 = self.longestCommonPrefix(strs[0:2])
            LCP_others = self.longestCommonPrefix(strs[2:])
            return self.longestCommonPrefix([LCP_2, LCP_others])
        elif len(strs) == 2:
            result = []
            length = min(len(strs[0]), len(strs[1]))
            for i in range(length):
                if strs[0][i] == strs[1][i]:
                    result.append(strs[0][i])
                else:
                    break
            return ''.join(result)


class OfficialSolution1:
    """Horizontal scanning"""
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == '':
                    return ''
        return prefix


class OfficialSolution2:
    """Vertical scanning"""
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            # i-th char in strs[0]
            c = strs[0][i]
            for j in range(1, len(strs)):
                # j-th string
                if i == len(strs[j]) or c != strs[j][i]:
                    return strs[0][: i]
        return strs[0]


class OfficialSolution3:
    """Divide and conquer"""
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        return self.LCP(strs, 0, len(strs) - 1)

    def LCP(self, strs, l, r):
        if l == r:
            return strs[l]
        else:
            mid = (l + r) // 2
            lcpLeft = self.LCP(strs, l, mid)
            lcpRight = self.LCP(strs, mid+1, r)
            return self.commonPrefix(lcpLeft, lcpRight)

    def commonPrefix(self, left, right):
        length = min(len(left), len(right))
        for i in range(length):
            if left[i] != right[i]:
                return left[: i]
        return left[: length]


class OfficialSolution4:
    """Binary search"""
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        minLen = min(map(len, strs))
        low = 0
        high = minLen
        while low <= high:
            mid = (low + high) // 2
            if self.isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][: mid]

    def isCommonPrefix(self, strs, length):
        str1 = strs[0][: length]
        for i in range(1, len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True


if __name__ == '__main__':
    lcp = Solution()
    lcp.longestCommonPrefix(["flower", "flow", "flight"])
