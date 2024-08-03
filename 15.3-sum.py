from typing import List, Optional

#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results_threeSum = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tgt = -nums[i]
            results_twoSum = self.twoSum(nums, tgt, i+1)
            for res_2 in results_twoSum:
                results_threeSum.append([nums[i], *res_2])
        return results_threeSum
    
    def twoSum(self, nums, target, start=0):
        results = []
        # for i in range(start, len(nums)):
        #     if i > start and nums[i] == nums[i-1]:
        #         continue
        #     for j in range(len(nums)-1, i, -1):
        #         if j < len(nums)-1 and nums[j] == nums[j+1]:
        #             continue
        #         if nums[i] + nums[j] == target:
        #             results.append([nums[i], nums[j]])

        i, j = start, len(nums) - 1
        while i < j:
            left, right = nums[i], nums[j]
            two_sum = left + right
            if two_sum < target:
                i += 1
            elif two_sum > target:
                j -= 1
            else:
                results.append([left, right])
                while i < j and nums[i] == left:
                    i += 1
                while i < j and nums[j] == right:
                    j -= 1
        return results
# @lc code=end


if __name__ == '__main__':
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))