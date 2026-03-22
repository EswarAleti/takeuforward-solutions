"""
714: Best Time to Buy and Sell Stock with Transaction Fee
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.


Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
"""

from typing import List


def maxProfit(prices: List[int], fee: int) -> int:
    """Maximum profit with transaction fee using space-optimized tabulation.

    Key difference: Fee is deducted when selling (not buying).
    prev[0] = max profit when not holding at previous day
    prev[1] = max profit when holding at previous day
    Uses two-row DP for space optimization.

    Args:
        prices: List of integers representing stock prices per day
        fee: Transaction fee per buy/sell transaction
    Returns:
        Maximum profit from unlimited transactions with fees
    Complexity:
        Time: O(n), Space: O(1)
    """
    # Only track previous and current day states
    prev = [0, 0]
    curr = [0, 0]

    # Fill from end to start
    for i in range(len(prices) - 1, -1, -1):
        # In holding state (buy=1): buy now or skip
        curr[1] = max(-prices[i] + prev[0], prev[1])
        # In not holding state (buy=0): sell now (minus fee) or skip
        curr[0] = max(prices[i] - fee + prev[1], prev[0])
        prev = curr

    return curr[1]


# Test cases for space-optimized tabulation
print(
    maxProfit([1, 3, 2, 8, 4, 9], 2)
)  # Output: 8 (buy at 1, sell at 8, buy at 4, sell at 9)
print(
    maxProfit([1, 3, 7, 5, 10, 3], 3)
)  # Output: 6 (buy at 1, sell at 7, buy at 5, sell at 10)
