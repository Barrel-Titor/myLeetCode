"""
https://leetcode.com/problems/merge-sorted-array/
"""
import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # new_array = [0] * (m + n)
        nums1_copy = nums1.copy()
        i = j = k = 0
        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        if i == m:
            for _k in range(k, m + n):
                nums1[_k] = nums2[j]
                j += 1
        else:
            for _k in range(k, m + n):
                nums1[_k] = nums1_copy[i]
                i += 1
        # return nums1


class leetchunhuiSolution:
    """
    https://leetcode.com/problems/merge-sorted-array/discuss/29522/This-is-my-AC-code-may-help-you
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


class tju_xu_Solution:
    """
    https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while n > 0:
            if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_eg1(self):
        paras = dict(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
        self.assertEqual([1, 2, 2, 3, 5, 6], self.sol.merge(**paras))

    def test_eg2(self):
        paras = dict(nums1=[1], m=1, nums2=[], n=0)
        self.assertEqual([1], self.sol.merge(**paras))


if __name__ == '__main__':
    unittest.main()
