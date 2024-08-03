from typing import List, Optional

#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.strip().split()
        return ' '.join(word_list[::-1])
# @lc code=end

