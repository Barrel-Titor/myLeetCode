"""
https://leetcode.com/problems/search-insert-position/
"""
from typing import List
import unittest


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lower = mid + 1
            else:
                upper = mid

        if target > nums[lower]:
            return lower + 1
        else:
            return lower


class cmcSolution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def searchInsertWithDuplicates(self, nums, target):
        # works even if there are duplicates.
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                if nums[mid] == target and nums[mid - 1] != target:
                    return mid
                else:
                    r = mid - 1
        return l


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_eg1(self):
        eg = dict(nums=[1, 3, 5, 6], target=5)
        self.assertEqual(self.sol.searchInsert(**eg), 2)

    def test_eg2(self):
        eg = dict(nums=[1, 3, 5, 6], target=2)
        self.assertEqual(self.sol.searchInsert(**eg), 1)

    def test_eg3(self):
        eg = dict(nums=[1, 3, 5, 6], target=7)
        self.assertEqual(self.sol.searchInsert(**eg), 4)

    def test_eg4(self):
        eg = dict(nums=[1, 3, 5, 6], target=0)
        self.assertEqual(self.sol.searchInsert(**eg), 0)

    def test_eg5(self):
        eg = dict(nums=[1], target=0)
        self.assertEqual(self.sol.searchInsert(**eg), 0)

    def test_wrong(self):
        eg = dict(nums=[1], target=1)
        self.assertEqual(self.sol.searchInsert(**eg), 0)

    def test_duplicates(self):
        cmcsol = cmcSolution()
        eg = dict(nums=[1, 1, 1, 1], target=1)
        self.assertEqual(cmcsol.searchInsertWithDuplicates(**eg), 0)


if __name__ == '__main__':
    unittest.main()
