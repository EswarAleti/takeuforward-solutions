"""
Unbounded knapsack problem - maximize value with unlimited items.

Given items with value and weight, and weight capacity, fill knapsack
to maximize total value. Each item can be taken unlimited times.

Note: Each item can be taken any number of times.

Input: val[] = [1, 1], wt[] = [2, 1], capacity = 3
Output: 3

Input: val[] = [10, 40, 50, 70], wt[] = [1, 3, 4, 5], capacity = 8
Output: 110

Input: val[] = [6, 8, 7, 100], wt[] = [2, 3, 4, 5], capacity = 1
Output: 0
"""


def knapSack2D(val, wt, capacity):
    """Unbounded knapsack using 2D DP.

    Uses 2D DP where dp[i][j] = max value using items 0..i with
    capacity j. Unlike 0/1 knapsack, each item can be used multiple
    times, so we recurse with same item (dp[i][j-wt[i]]).

    Args:
        val: List of item values
        wt: List of item weights
        capacity: Maximum weight capacity

    Returns:
        Maximum value achievable within capacity

    Complexity:
        Time: O(n * capacity), Space: O(n * capacity)
    """
    n = len(val)
    # DP table: dp[i][j] = max value using items 0..i with capacity j
    dp = [[0] * (capacity + 1) for _ in range(n)]

    # Fill DP table
    for i in range(n):
        for j in range(capacity + 1):
            # Don't take current item
            dp[i][j] = dp[i - 1][j]
            # Take current item if it fits (unlimited times)
            if wt[i] <= j:
                dp[i][j] = max(dp[i][j], val[i] + dp[i][j - wt[i]])

    return dp[-1][-1]


# Test cases for 2D DP approach
print(knapSack2D([1, 1], [2, 1], 3))  # Output: 3
print(knapSack2D([10, 40, 50, 70], [1, 3, 4, 5], 8))  # Output: 110
print(knapSack2D([6, 8, 7, 100], [2, 3, 4, 5], 1))  # Output: 0


def knapSack1D(val, wt, capacity):
    """Unbounded knapsack using 1D DP (space-optimized).

    Uses 1D DP where dp[j] = max value with capacity j. For each item,
    iterate forward (not backward like 0/1 knapsack) to allow using
    same item multiple times.

    Args:
        val: List of item values
        wt: List of item weights
        capacity: Maximum weight capacity

    Returns:
        Maximum value achievable within capacity

    Complexity:
        Time: O(n * capacity), Space: O(capacity)
    """
    n = len(val)
    # DP array: dp[j] = max value with capacity j
    dp = [0] * (capacity + 1)

    # For each item (can be used multiple times)
    for i in range(n):
        # Iterate forward to allow reusing same item
        for j in range(capacity + 1):
            # Take item if it fits (can take multiple times)
            if wt[i] <= j:
                dp[j] = max(dp[j], val[i] + dp[j - wt[i]])

    return dp[-1]


# Test cases for 1D DP approach
print(knapSack1D([1, 1], [2, 1], 3))  # Output: 3
print(knapSack1D([10, 40, 50, 70], [1, 3, 4, 5], 8))  # Output: 110
print(knapSack1D([6, 8, 7, 100], [2, 3, 4, 5], 1))  # Output: 0
