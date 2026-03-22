"""
188. Best Time to Buy and Sell Stock IV
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

from typing import List


def maxProfit(k: int, prices: List[int]) -> int:
    """Maximum profit with at most k transactions using space optimization.

    Generalization of stock problems to allow up to k transactions.
    Uses tabulation with space optimization: only track prev and curr day states.
    Reduces space from O(n*2*(k+1)) to O(2*(k+1)).

    Args:
        k: Maximum number of transactions allowed
        prices: List of integers representing stock prices per day
    Returns:
        Maximum profit from at most k transactions
    Complexity:
        Time: O(n*2*k), Space: O(1) (constant for given k)
    """
    n = len(prices)
    # Only track previous and current day states for each buy state and transaction cap
    prev = [[0] * (k + 1) for _ in range(2)]
    curr = [[0] * (k + 1) for _ in range(2)]

    # Fill from end to start
    for i in range(n - 1, -1, -1):
        for buy in range(2):
            for cap in range(1, k + 1):
                if buy:
                    # In holding state: buy now or skip
                    curr[buy][cap] = max(-prices[i] + prev[0][cap], prev[1][cap])
                else:
                    # In not holding state: sell now or skip
                    curr[buy][cap] = max(prices[i] + prev[1][cap - 1], prev[0][cap])
        prev = curr
    return curr[1][k]


# Test cases for Tabulation with space optimization
print(
    maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4])
)  # Output: 6 (buy at 0, sell at 3, buy at 1, sell at 4)
print(maxProfit(2, [1, 2, 3, 4, 5]))  # Output: 4 (buy at 1, sell at 5)
print(maxProfit(2, [7, 6, 4, 3, 1]))  # Output: 0 (no profit possible)
print(maxProfit(2, [2, 4, 1]))  # Output: 2 (buy at 2, sell at 4)
print(
    maxProfit(2, [3, 2, 6, 5, 0, 3])
)  # Output: 7 (buy at 2, sell at 6, buy at 0, sell at 3)
