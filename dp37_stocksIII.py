"""
123. Best Time to Buy and Sell Stock III
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""

from functools import lru_cache
from typing import List


def maxProfit(prices: List[int]) -> int:
    """Approach 1: Memoization with @lru_cache.

    Time: O(n*2*3), Space: O(n*2*3) for cache.
    """

    @lru_cache
    def recursion(i, buy, cap):
        # Base case: reached end or used both transactions
        if i == len(prices) or cap == 0:
            return 0

        if buy:
            # Can buy (spend money) or skip
            return max(-prices[i] + recursion(i + 1, 0, cap), recursion(i + 1, 1, cap))
        else:
            # Can sell (gain money) or skip
            return max(
                prices[i] + recursion(i + 1, 1, cap - 1), recursion(i + 1, 0, cap)
            )

    return recursion(0, 1, 2)


# Test cases for Approach 1
print(
    maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
)  # Output: 6 (buy at 0, sell at 3, buy at 1, sell at 4)
print(maxProfit([1, 2, 3, 4, 5]))  # Output: 4 (buy at 1, sell at 5)
print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0 (no profit possible)


# Approach 2: Memoization with manual DP table
def maxProfit(prices: List[int]) -> int:
    """Manual memoization approach using 3D DP table.

    dp[i][buy][cap] = max profit from day i, buy state, and remaining transactions.
    Time: O(n*2*2), Space: O(n*2*2).
    """
    dp = [[[-1] * 2 for _ in range(2)] for _ in range(len(prices))]

    def recursion(i, buy, cap):
        if i == len(prices) or cap == 0:
            return 0

        # Return cached result if available
        if dp[i][buy][cap - 1] != -1:
            return dp[i][buy][cap - 1]

        if buy:
            dp[i][buy][cap - 1] = max(
                -prices[i] + recursion(i + 1, 0, cap), recursion(i + 1, 1, cap)
            )
        else:
            dp[i][buy][cap - 1] = max(
                prices[i] + recursion(i + 1, 1, cap - 1), recursion(i + 1, 0, cap)
            )
        return dp[i][buy][cap - 1]

    return recursion(0, 1, 2)


# Test cases for Approach 2
print(
    maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
)  # Output: 6 (buy at 0, sell at 3, buy at 1, sell at 4)
print(maxProfit([1, 2, 3, 4, 5]))  # Output: 4 (buy at 1, sell at 5)
print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0 (no profit possible)


# Approach 3: Tabulation (bottom-up DP)
def maxProfit(prices: List[int]) -> int:
    """Tabulation (iterative DP) approach.

    dp[i][buy][cap] = max profit from day i with buy state and transactions cap.
    Time: O(n*2*2), Space: O(n*2*2).
    """
    n = len(prices)
    max_cap = 2
    # dp[i][buy][cap]: day i, buy state (0=can buy, 1=can sell), remaining transactions
    dp = [[[0] * (max_cap + 1) for _ in range(2)] for _ in range(n + 1)]

    # Fill table from end to start
    for i in range(n - 1, -1, -1):
        for buy in range(2):
            for cap in range(1, max_cap + 1):
                if buy:
                    # In buying state: buy now or skip
                    dp[i][buy][cap] = max(
                        -prices[i] + dp[i + 1][0][cap], dp[i + 1][1][cap]
                    )
                else:
                    # In selling state: sell now or skip
                    dp[i][buy][cap] = max(
                        prices[i] + dp[i + 1][1][cap - 1], dp[i + 1][0][cap]
                    )

    return dp[0][1][2]


# Test cases for Approach 3
print(
    maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
)  # Output: 6 (buy at 0, sell at 3, buy at 1, sell at 4)
print(maxProfit([1, 2, 3, 4, 5]))  # Output: 4 (buy at 1, sell at 5)
print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0 (no profit possible)


def maxProfit(prices: List[int]) -> int:
    """Approach 4: Tabulation with space optimization.

    Instead of storing entire 3D DP table, use only two rows (prev, curr) since
    each state only depends on the next day. Reduces space from O(n*2*3) to O(2*3).

    Time: O(n*2*2), Space: O(1) (constant for max_cap=2).
    """
    n = len(prices)
    max_cap = 2
    # Only track previous and current day states
    prev = [[0] * (max_cap + 1) for _ in range(2)]
    curr = [[0] * (max_cap + 1) for _ in range(2)]

    # Fill from end to start
    for i in range(n - 1, -1, -1):
        for buy in range(2):
            for cap in range(1, max_cap + 1):
                if buy:
                    # In buying state: buy now or skip
                    curr[buy][cap] = max(-prices[i] + prev[0][cap], prev[1][cap])
                else:
                    # In selling state: sell now or skip
                    curr[buy][cap] = max(prices[i] + prev[1][cap - 1], prev[0][cap])
        prev = curr
    return curr[1][2]


# Test cases for Approach 4 (Space Optimized Tabulation)
print(
    maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
)  # Output: 6 (buy at 0, sell at 3, buy at 1, sell at 4)
print(maxProfit([1, 2, 3, 4, 5]))  # Output: 4 (buy at 1, sell at 5)
print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0 (no profit possible)
