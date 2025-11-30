"""Unique Paths in a Grid.

Given integers m and n (rows and columns), return the number of unique
paths from top-left (0, 0) to bottom-right (m-1, n-1). Movement is allowed
only right or down.

Examples:
    m=3, n=2 -> 3
    m=2, n=4 -> 4
"""


def uniquePaths(m, n):
    """Return number of unique paths in m x n grid.

    Args:
        m (int): number of rows
        n (int): number of columns

    Returns:
        int: total unique paths from (0,0) to (m-1,n-1)

    Complexity: Time O(m*n), Space O(m*n)
    """
    # dp[i][j] = number of ways to reach cell (i, j)
    dp = [[0] * n for _ in range(m)]

    # Fill first row and column (only 1 way to reach them)
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                # Ways to reach (i,j) = from top + from left
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


print(uniquePaths(2, 2))  # Output: 2
print(uniquePaths(3, 2))  # Output: 3
print(uniquePaths(2, 4))  # Output: 4
print(uniquePaths(3, 3))  # Output: 6
print(uniquePaths(4, 4))  # Output: 20


def uniquePathsInplace(m, n):
    """Return unique paths using O(n) space optimization.

    Uses a 1D array instead of 2D by updating in-place.

    Args:
        m (int): number of rows
        n (int): number of columns

    Returns:
        int: total unique paths from (0,0) to (m-1,n-1)

    Complexity: Time O(m*n), Space O(n)
    """
    # dp[j] represents the number of ways to reach current row, column j
    dp = [1] * n

    # For each row after the first
    for _ in range(1, m):
        # For each column after the first, update with sum of top+left
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]

    return dp[-1]


print(uniquePathsInplace(2, 2))  # Output: 2
print(uniquePathsInplace(3, 2))  # Output: 3
print(uniquePathsInplace(2, 4))  # Output: 4
print(uniquePathsInplace(3, 3))  # Output: 6
print(uniquePathsInplace(4, 4))  # Output: 20
