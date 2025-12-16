"""
Rod cutting problem - maximize revenue by cutting rod into pieces.

Given rod of length n and price array where price[i] is value of
length i piece, determine maximum revenue by cutting optimally.
Can choose not to cut (sell as whole) or cut into smaller pieces.

Example: price = [1, 5, 8, 9, 10, 17, 17, 20], n = 8
- Cut into 2 pieces of length 4: 2 * 10 = 20
- Cut into pieces of 2,2,2,2: 4 * 5 = 20
- Optimal: pieces of 2 and 6 = 5 + 17 = 22
- Output: 22
"""


def cutRod2D(price):
    """Rod cutting using 2D DP (unbounded knapsack variant).

    Uses 2D DP where dp[i][j] = max value cutting rod of length j
    using pieces of size 1 to i. For each piece size i, either don't
    cut or use it (recurse with remaining length).

    Args:
        price: List where price[i] = value of piece of length i+1

    Returns:
        Maximum revenue obtainable from rod

    Complexity:
        Time: O(n^2) where n = len(price)
        Space: O(n^2) for 2D DP array
    """
    n = len(price)
    # DP table: dp[i][j] = max value for rod of length j using pieces 1..i
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Base case: for rod of each length, can sell as single piece
    for i in range(1, n + 1):
        dp[0][i] = price[i - 1]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Don't cut piece of size i (take value without this piece)
            dp[i][j] = dp[i - 1][j]
            # Cut piece of size i if it fits in rod of length j
            if i < j:
                # Use piece i and recurse with remaining length
                dp[i][j] = max(dp[i][j], dp[i][j - i] + price[i - 1])

    return dp[-1][-1]


# Test cases for 2D DP approach
print(cutRod2D([2, 5, 7, 8, 10]))  # Output: 12
print(cutRod2D([1, 5, 8, 9, 10, 17, 17, 20]))  # Output: 22
print(cutRod2D([3, 5, 8, 9, 10, 17, 17, 20]))  # Output: 24
print(cutRod2D([3]))  # Output: 3


def cutRod1D(price):
    """Rod cutting using 1D DP (space-optimized).

    Uses 1D DP where dp[j] = max value cutting rod of length j.
    For each piece size i, update all possible rod lengths that can
    use this piece.

    Args:
        price: List where price[i] = value of piece of length i+1

    Returns:
        Maximum revenue obtainable from rod

    Complexity:
        Time: O(n^2) where n = len(price)
        Space: O(n) for 1D DP array
    """
    n = len(price)
    # DP array: dp[j] = max value for rod of length j
    dp = [0] * n

    # Initialize: each rod length can be sold as single piece
    for i in range(n):
        dp[i] = price[i]

    # For each piece size
    for i in range(1, n):
        # Update all rod lengths that can use this piece
        for j in range(i, n):
            # Max of not cutting or cutting piece of size i
            dp[j] = max(dp[j], dp[j - i] + price[i - 1])

    return dp[-1]


# Test cases for 1D DP approach
print(cutRod1D([2, 5, 7, 8, 10]))  # Output: 12
print(cutRod1D([1, 5, 8, 9, 10, 17, 17, 20]))  # Output: 22
print(cutRod1D([3, 5, 8, 9, 10, 17, 17, 20]))  # Output: 24
print(cutRod1D([3]))  # Output: 3
