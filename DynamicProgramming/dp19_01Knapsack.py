"""
0/1 Knapsack problem - maximize value within weight capacity.

Given items with value and weight, pack knapsack to maximize total
value without exceeding capacity W. Each item can be included or
excluded completely (no fractional selection).

Example: W = 5, val = [10, 40, 30, 50], wt = [5, 4, 2, 3]
- Take items 1, 3: weight = 7 (exceeds)
- Take items 1, 2: weight = 5, value = 80
- Output: 80
"""


def knapsack01(W, wt, val):
    """Knapsack using pure recursion (exponential).

    Args:
        W: Maximum weight capacity
        wt: List of item weights
        val: List of item values

    Returns:
        Maximum value achievable

    Complexity:
        Time: O(2^n), Space: O(n) recursion depth
    """

    def recursion(i, rem_wt):
        # Base case: only first item available
        if i == 0:
            return val[i] if wt[i] <= rem_wt else 0

        # Exclude current item
        not_take = recursion(i - 1, rem_wt)

        # Include current item if within capacity
        take = 0
        if wt[i] <= rem_wt:
            take = val[i] + recursion(i - 1, rem_wt - wt[i])

        return max(take, not_take)

    return recursion(len(val) - 1, W)


# Test cases for recursion approach
print(knapsack01(4, [4, 5, 1], [1, 2, 3]))  # Output: 3
print(knapsack01(3, [4, 5, 6], [1, 2, 3]))  # Output: 0
print(knapsack01(5, [5, 4, 2, 3], [10, 40, 30, 50]))  # Output: 80


def knapsackMemoization(W, val, wt):
    """Knapsack using memoized recursion.

    Args:
        W: Maximum weight capacity
        val: List of item values
        wt: List of item weights

    Returns:
        Maximum value achievable

    Complexity:
        Time: O(n*W), Space: O(n*W) DP table
    """
    n = len(val)
    # DP table: dp[i][j] = max value using items 0..i with capacity j
    dp = [[-1] * (W + 1) for _ in range(n)]

    def recursion(i, rem_wt):
        # Base case: only first item available
        if i == 0:
            return val[0] if wt[0] <= rem_wt else 0

        # Return memoized result if available
        if dp[i][rem_wt] != -1:
            return dp[i][rem_wt]

        # Exclude current item
        not_take = recursion(i - 1, rem_wt)

        # Include current item if within capacity
        take = 0
        if wt[i] <= rem_wt:
            take = val[i] + recursion(i - 1, rem_wt - wt[i])

        # Store and return max value
        dp[i][rem_wt] = max(take, not_take)
        return dp[i][rem_wt]

    return recursion(n - 1, W)


# Test cases for memoization approach
print(knapsackMemoization(4, [1, 2, 3], [4, 5, 1]))  # Output: 3
print(knapsackMemoization(3, [1, 2, 3], [4, 5, 6]))  # Output: 0
print(knapsackMemoization(5, [10, 40, 30, 50], [5, 4, 2, 3]))  # Output: 80


def knapsackDP(W, val, wt):
    """Knapsack using bottom-up DP (space-optimized).

    Args:
        W: Maximum weight capacity
        val: List of item values
        wt: List of item weights

    Returns:
        Maximum value achievable

    Complexity:
        Time: O(n*W), Space: O(W) 1D DP array
    """
    n = len(val)
    # DP array: dp[j] = max value with capacity j
    dp = [0] * (W + 1)

    # Initialize with first item
    for j in range(wt[0], W + 1):
        dp[j] = val[0]

    # Process remaining items
    for i in range(1, n):
        # Iterate backwards to avoid using updated values
        for j in range(W, -1, -1):
            # Max value without current item
            no_take = dp[j]

            # Max value with current item (if fits)
            take = 0
            if wt[i] <= j:
                take = val[i] + dp[j - wt[i]]

            # Update with max
            dp[j] = max(take, no_take)

    return dp[-1]


# Test cases for bottom-up DP approach
print(knapsackDP(4, [1, 2, 3], [4, 5, 1]))  # Output: 3
print(knapsackDP(3, [1, 2, 3], [4, 5, 6]))  # Output: 0
print(knapsackDP(5, [10, 40, 30, 50], [5, 4, 2, 3]))  # Output: 80
