"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """brute force"""
        max_profit = 0
        for i_buy in range(len(prices)):
            for i_sell in range(i_buy+1, len(prices)):
                profit = prices[i_sell] - prices[i_buy]
                max_profit = max(max_profit, profit)
        return max_profit


class labuladongSolution:
    """
    ⼀个⽅法团灭LeetCode股票买卖问题
    今天手上没股票的状态：
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                   继续不持有   卖掉昨天持有的
    今天手上有股票的状态：
    dp[i][1] = max(dp[i-1][1], -prices[i])
                   继续持有     今天买进
    """
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0
        dp_i_1 = -inf
        for p in prices:
            dp_i_0 = max(dp_i_0, dp_i_1 + p)
            dp_i_1 = max(dp_i_1, -p)
        return dp_i_0


class OfficialSolution2:
    """one pass
    The points of interest are the peaks and valleys in the given graph. 
    We need to find the largest peak following the smallest valley. 
    We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = inf
        for current in prices:
            if current < min_price:
                min_price = current
            elif current - min_price > max_profit:
                max_profit = current - min_price
        return max_profit


if __name__ == '__main__':
    sol = Solution()
    testcase1 = [7,1,5,3,6,4]
    testcase2 = [7,6,4,3,1]
    testcase3 = [1]
    testcase4 = [1,2]
    print(sol.maxProfit(testcase1))
    print(sol.maxProfit(testcase2))
    print(sol.maxProfit(testcase3))
    print(sol.maxProfit(testcase4))
