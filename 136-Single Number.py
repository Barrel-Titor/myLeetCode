"""
https://leetcode.com/problems/single-number/
"""
from typing import List
from collections import Counter
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # record = dict()
        # for num in nums:
        #     record[num] = record.get(num, 0) + 1
        record = Counter(nums)
        for k, v in record.items():
            if v == 1:
                return k


class IvantsangSolution:
    """using XOR
    https://leetcode.com/problems/single-number/discuss/42997/My-O(n)-solution-using-XOR
    https://leetcode.com/problems/single-number/discuss/43201/Easy-Java-solution-(tell-you-why-using-bitwise-XOR)

    we have to know the bitwise XOR:
    0 ^ N = N
    N ^ N = 0
    commutative, a ^ b = b ^ a

    Let's say we have an array - [2,1,4,5,2,4,1]
    What we are doing is essentially this -
    => 0 ^ 2 ^ 1 ^ 4 ^ 5 ^ 2 ^ 4 ^ 1
    => 0 ^ (2 ^ 2) ^ (1 ^ 1) ^ (4 ^ 4) ^ 5 (Rearranging)
    => 0 ^ 0 ^ 0 ^ 0 ^ 5
    => 0 ^ 5
    => 5
    """
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


class OldCodingFarmerSolution:
    """
    https://leetcode.com/problems/single-number/discuss/43000/Python-different-solutions.
    """
    def singleNumber3(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
    
    def singleNumber4(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)