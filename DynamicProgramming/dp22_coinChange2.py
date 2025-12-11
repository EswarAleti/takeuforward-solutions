"""
Coin change II problem - count combinations to make amount.

Given coins of different denominations and target amount, count the
number of different combinations that sum to amount. Each coin can be
used unlimited times. Order doesn't matter (combinations not permutations).

Example: amount = 5, coins = [1, 2, 5]
- Combinations: {5}, {2,2,1}, {2,1,1,1}, {1,1,1,1,1}
- Output: 4
"""

from typing import List


def change2D(amount: int, coins: List[int]) -> int:
    """Count coin combinations using 2D DP (combinations approach).

    Uses 2D DP where dp[i][j] = count of ways to make amount j using
    coins[0..i]. For each coin, either exclude it (take from above) or
    include it (add current coin combinations).

    Args:
        amount: Target amount to make
        coins: List of coin denominations

    Returns:
        Number of combinations to make target amount

    Complexity:
        Time: O(n * amount) where n = len(coins)
        Space: O(n * amount) for 2D DP array
    """
    n = len(coins)
    # DP table: dp[i][j] = count of ways to make amount j using coins[0..i]
    dp = [[0] * (amount + 1) for _ in range(n)]

    # Base case: amount 0 can be made in 1 way (no coins)
    for i in range(n):
        dp[i][0] = 1

    # Fill DP table iterating by amount then by coin
    for j in range(amount + 1):
        for i in range(n):
            # Exclude current coin
            dp[i][j] = dp[i - 1][j]
            # Include current coin if possible
            if coins[i] <= j:
                dp[i][j] += dp[i][j - coins[i]]

    return dp[-1][-1]


# Test cases for 2D DP approach
print(change2D(5, [1, 2, 5]))  # Output: 4
print(change2D(3, [2]))  # Output: 0
print(change2D(10, [10]))  # Output: 1


def change1D(amount: int, coins: List[int]) -> int:
    """Count coin combinations using 1D DP (space-optimized).

    Uses 1D DP where dp[j] = count of ways to make amount j. Iterates
    coins in outer loop to avoid counting permutations (order doesn't
    matter). For each coin, update all amounts it contributes to.

    Args:
        amount: Target amount to make
        coins: List of coin denominations

    Returns:
        Number of combinations to make target amount

    Complexity:
        Time: O(n * amount) where n = len(coins)
        Space: O(amount) 1D DP array
    """
    n = len(coins)
    # DP array: dp[j] = count of ways to make amount j
    dp = [0] * (amount + 1)
    # Base case: amount 0 can be made in 1 way
    dp[0] = 1

    # For each coin denomination
    for coin in coins:
        # Update all amounts this coin can contribute to
        for target in range(coin, amount + 1):
            # Add combinations using current coin
            dp[target] += dp[target - coin]

    return dp[-1]


# Test cases for 1D DP approach
print(change1D(5, [1, 2, 5]))  # Output: 4
print(change1D(3, [2]))  # Output: 0
print(change1D(10, [10]))  # Output: 1
