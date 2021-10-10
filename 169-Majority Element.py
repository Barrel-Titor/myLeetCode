"""
https://leetcode.com/problems/majority-element/
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = dict()
        threshold = len(nums) // 2
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
            if counts[n] > threshold:
                return n


class OfficialSolution6:
    """https://leetcode.com/problems/majority-element/solution/
    Boyer-Moore Voting Algorithm

    we maintain a count, which is incremented whenever we see an instance of our current candidate for majority element and decremented whenever we see anything else. Whenever count equals 0, we effectively forget about everything in nums up to the current index and consider the current number as the candidate for majority element. 

    eg:
    [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
    [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 5, 5, 5, 5]

    Therefore, given that it is impossible (in both cases) to discard more majority elements than minority elements, we are safe in discarding the prefix and attempting to recursively solve the majority element problem for the suffix. Eventually, a suffix will be found for which count does not hit 0, and the majority element of that suffix will necessarily be the same as the majority element of the overall array
    """
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            count += (1 if n == candidate else -1)
        return candidate
