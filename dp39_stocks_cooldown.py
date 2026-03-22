"""
309. Best Time to Buy and Sell Stock with Cooldown
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
"""

from functools import lru_cache
from typing import List


def maxProfit(prices: List[int]) -> int:
    """Approach 1: Memoization with @lru_cache.

    Key difference: After selling, must skip next day (cooldown).
    When selling (not holding), recurse with i+2 instead of i+1.

    Time: O(n), Space: O(n) for memoization cache.
    """

    @lru_cache
    def recursion(i, buy):
        # Base case: reached end of prices
        if i >= len(prices):
            return 0

        if buy:
            # Can buy (spend money) or skip
            return max(-prices[i] + recursion(i + 1, 0), recursion(i + 1, 1))
        else:
            # Can sell (gain money, then skip next day as cooldown) or skip
            return max(prices[i] + recursion(i + 2, 1), recursion(i + 1, 0))

    return recursion(0, 1)


# Test cases for Approach 1 (Memoization)
print(
    maxProfit([1, 2, 3, 0, 2])
)  # Output: 3 (buy at 1, sell at 3, cooldown, buy at 0, sell at 2)
print(maxProfit([1]))  # Output: 0 (no profit possible)


def maxProfit(prices: List[int]) -> int:
    """Approach 2: Tabulation (bottom-up DP).

    dp[i][0] = max profit when not holding at day i
    dp[i][1] = max profit when holding at day i
    Note: dp table size is n+2 to handle cooldown (i+2 lookups).

    Time: O(n), Space: O(n) for DP table.
    """
    n = len(prices)
    # Extra row for cooldown boundary handling
    dp = [[0] * 2 for _ in range(n + 2)]

    # Fill from end to start
    for i in range(n - 1, -1, -1):
        for buy in range(2):
            if buy:
                # In holding state: buy now or skip
                dp[i][buy] = max(-prices[i] + dp[i + 1][0], dp[i + 1][1])
            else:
                # In not holding state: sell now (skip next day due to cooldown) or skip
                dp[i][buy] = max(prices[i] + dp[i + 2][1], dp[i + 1][0])
    return dp[0][1]


# Test cases for Approach 2 (Tabulation)
print(
    maxProfit([1, 2, 3, 0, 2])
)  # Output: 3 (buy at 1, sell at 3, cooldown, buy at 0, sell at 2)
print(maxProfit([1]))  # Output: 0 (no profit possible)


def maxProfit(prices: List[int]) -> int:
    """Approach 3: Tabulation without buy loop.

    Simplify by directly computing dp[i][1] and dp[i][0] without the buy loop,
    since buy states are always 0 or 1.

    Time: O(n), Space: O(n) for DP table.
    """
    n = len(prices)
    # dp table with extra rows for cooldown boundary
    dp = [[0] * 2 for _ in range(n + 2)]

    # Fill from end to start
    for i in range(n - 1, -1, -1):
        # In holding state (buy=1): buy now or skip
        dp[i][1] = max(-prices[i] + dp[i + 1][0], dp[i + 1][1])
        # In not holding state (buy=0): sell now (cooldown, use i+2) or skip
        dp[i][0] = max(prices[i] + dp[i + 2][1], dp[i + 1][0])
    return dp[0][1]


# Test cases for Approach 3 (Simplified tabulation)
print(
    maxProfit([1, 2, 3, 0, 2])
)  # Output: 3 (buy at 1, sell at 3, cooldown, buy at 0, sell at 2)
print(maxProfit([1]))  # Output: 0 (no profit possible)
