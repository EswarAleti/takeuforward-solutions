"""
Coin change problem - minimum coins to make amount.

Given coins of different denominations and a target amount, find the
fewest number of coins needed to make that amount. Each coin can be
used unlimited times. Return -1 if impossible.

Example: coins = [1, 2, 5], amount = 11
- Use 5 + 5 + 1 = 11 with 3 coins
- Optimal: 5 + 5 + 1 (3 coins)
- Output: 3
"""

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    """Minimum coins needed to make target amount.

    Uses bottom-up DP where dp[i] represents the minimum number of coins
    needed to make amount i. For each coin, update all amounts it can
    contribute to.

    Args:
        coins: List of coin denominations
        amount: Target amount to make

    Returns:
        Minimum number of coins needed, or -1 if impossible

    Complexity:
        Time: O(amount * n) where n = len(coins)
        Space: O(amount) for DP array
    """
    # DP array: dp[i] = min coins needed to make amount i
    dp = [float("inf")] * (amount + 1)
    # Base case: 0 coins needed for amount 0
    dp[0] = 0

    # For each coin denomination
    for coin in coins:
        # Update all amounts that can be formed using this coin
        for tgt in range(1, amount + 1):
            # If coin value <= target amount, we can use this coin
            if coin <= tgt:
                # Take min of not using or using this coin
                dp[tgt] = min(dp[tgt], 1 + dp[tgt - coin])

    # Return result or -1 if impossible
    return -1 if dp[-1] == float("inf") else dp[-1]


# Test cases
print(coinChange([1, 2, 5], 11))  # Output: 3
print(coinChange([2], 3))  # Output: -1
print(coinChange([1], 0))  # Output: 0
