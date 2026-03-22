"""
Best time to buy and sell stock (unlimited transactions).

Given stock prices for each day, find the maximum profit from unlimited buy-sell transactions.
You can only hold at most one share at any time. You can buy and sell on the same day.

Example: prices = [7, 1, 5, 3, 6, 4]
- Buy at 1, sell at 5 (profit = 4)
- Buy at 3, sell at 6 (profit = 3)
- Total profit = 7
"""

from functools import lru_cache
from typing import List


def maxProfitMemoization(prices: List[int]) -> int:
    """Maximum profit using memoized recursion (top-down DP).

    At each day, decide: buy (move to holding state), sell (move to not holding state),
    or skip. Cache states to avoid recomputation.
    State: (day index, holding stock or not).

    Args:
        prices: List of integers representing stock prices per day
    Returns:
        Maximum profit from unlimited transactions
    Complexity:
        Time: O(n), Space: O(n) for memoization cache
    """

    @lru_cache
    def recursion(i, buy):
        # Base case: reached end of prices
        if i == len(prices):
            return 0
        # If we can buy: either buy today or skip buying
        if buy:
            return max(-prices[i] + recursion(i + 1, 0), recursion(i + 1, 1))
        # If we can sell: either sell today or skip selling
        else:
            return max(prices[i] + recursion(i + 1, 1), recursion(i + 1, 0))

    return recursion(0, 1)


# Test cases for Approach 1 (Memoization)
print(
    maxProfitMemoization([7, 1, 5, 3, 6, 4])
)  # Output: 7 (buy at 1, sell at 5, buy at 3, sell at 6)
print(maxProfitMemoization([1, 2, 3, 4, 5]))  # Output: 4 (buy at 1, sell at 5)
print(maxProfitMemoization([7, 6, 4, 3, 1]))  # Output: 0 (no profit possible)


def maxProfitDP(prices: List[int]) -> int:
    """Maximum profit using bottom-up DP (memoization with explicit table).

    Use explicit DP table instead of function memoization decorator.
    dp[i][0] = max profit when not holding stock at day i
    dp[i][1] = max profit when holding stock at day i

    Args:
        prices: List of integers representing stock prices per day
    Returns:
        Maximum profit from unlimited transactions
    Complexity:
        Time: O(n), Space: O(n) for DP table
    """
    dp = [[-1] * 2 for _ in range(len(prices))]

    def recursion(i, buy):
        # Base case: reached end of prices
        if i == len(prices):
            return 0
        # Return cached result if available
        if dp[i][buy] != -1:
            return dp[i][buy]
        # If we can buy: either buy today or skip buying
        if buy:
            dp[i][buy] = max(-prices[i] + recursion(i + 1, 0), recursion(i + 1, 1))
        # If we can sell: either sell today or skip selling
        else:
            dp[i][buy] = max(prices[i] + recursion(i + 1, 1), recursion(i + 1, 0))
        return dp[i][buy]

    return recursion(0, 1)


# Test cases for Approach 2 (Manual Memoization)
print(
    maxProfitDP([7, 1, 5, 3, 6, 4])
)  # Output: 7 (buy at 1, sell at 5, buy at 3, sell at 6)
print(maxProfitDP([1, 2, 3, 4, 5]))  # Output: 4 (buy at 1, sell at 5)
print(maxProfitDP([7, 6, 4, 3, 1]))  # Output: 0 (no profit possible)


def maxProfit(prices: List[int]) -> int:
    """Maximum profit using tabulation (bottom-up DP).

    dp[i][0] = max profit when not holding stock at day i
    dp[i][1] = max profit when holding stock at day i
    Build table iteratively from end to start.

    Args:
        prices: List of integers representing stock prices per day
    Returns:
        Maximum profit from unlimited transactions
    Complexity:
        Time: O(n), Space: O(n) for DP table
    """
    n = len(prices)
    # dp[i][buy]: day i, 0=not holding, 1=holding stock
    dp = [[0] * 2 for _ in range(n + 1)]

    # Fill table from end to start
    for i in range(n - 1, -1, -1):
        for buy in range(2):
            if buy:
                # In holding state: buy today or skip
                dp[i][buy] = max(-prices[i] + dp[i + 1][0], dp[i + 1][1])
            else:
                # In not holding state: sell today or skip
                dp[i][buy] = max(prices[i] + dp[i + 1][1], dp[i + 1][0])
    return dp[0][1]


# Test cases for Approach 3 (Tabulation)
print(
    maxProfit([7, 1, 5, 3, 6, 4])
)  # Output: 7 (buy at 1, sell at 5, buy at 3, sell at 6)
print(maxProfit([1, 2, 3, 4, 5]))  # Output: 4 (buy at 1, sell at 5)
print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0 (no profit possible)


def maxProfit(prices: List[int]) -> int:
    """Maximum profit using tabulation with space optimization.

    Instead of storing entire DP table, use only two rows (prev, curr) since
    each state only depends on the next day. Reduces space from O(n) to O(1).

    Args:
        prices: List of integers representing stock prices per day
    Returns:
        Maximum profit from unlimited transactions
    Complexity:
        Time: O(n), Space: O(1)
    """
    n = len(prices)
    # Only track previous and current day states
    prev = [0, 0]
    curr = [0, 0]

    # Fill from end to start
    for i in range(n - 1, -1, -1):
        for buy in range(2):
            if buy:
                # In holding state: buy today or skip
                curr[buy] = max(-prices[i] + prev[0], prev[1])
            else:
                # In not holding state: sell today or skip
                curr[buy] = max(prices[i] + prev[1], prev[0])
        prev = curr
    return curr[1]


# Test cases for Approach 4 (Tabulation with space optimization)
print(
    maxProfit([7, 1, 5, 3, 6, 4])
)  # Output: 7 (buy at 1, sell at 5, buy at 3, sell at 6)
print(maxProfit([1, 2, 3, 4, 5]))  # Output: 4 (buy at 1, sell at 5)
print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0 (no profit possible)


# Approach 5: Greedy
def maxProfitGreedy(prices: List[int]) -> int:
    """Maximum profit using greedy approach.

    Capitalize on every upward price movement. If price goes up from day i to i+1,
    buy at i and sell at i+1 to capture that profit. Sum all positive differences.

    Args:
        prices: List of integers representing stock prices per day
    Returns:
        Maximum profit from unlimited transactions
    Complexity:
        Time: O(n), Space: O(1)
    """
    profit = 0
    # Capture profit from every upward price movement
    for i in range(1, len(prices)):
        profit += max(0, prices[i] - prices[i - 1])
    return profit


# Test cases for Approach 5 (Greedy)
print(
    maxProfitGreedy([7, 1, 5, 3, 6, 4])
)  # Output: 7 (buy at 1, sell at 5, buy at 3, sell at 6)
print(maxProfitGreedy([1, 2, 3, 4, 5]))  # Output: 4 (buy at 1, sell at 5)
print(maxProfitGreedy([7, 6, 4, 3, 1]))  # Output: 0 (no profit possible)
