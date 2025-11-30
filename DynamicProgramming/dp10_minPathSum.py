"""Minimum Path Sum in Grid.

Given an m x n grid with non-negative numbers, find the path from top-left
to bottom-right that minimizes the sum. Only right and down moves allowed.

Examples:
    grid = [[1,3,1],[1,5,1],[4,2,1]] -> 7
    grid = [[1,2,3],[4,5,6]] -> 12
"""


def minPathSum(grid):
    """Return minimum path sum from top-left to bottom-right.

    Args:
        grid (List[List[int]]): m x n grid of non-negative integers

    Returns:
        int: minimum sum along any path

    Complexity: Time O(m*n), Space O(m*n)
    """
    m, n = len(grid), len(grid[0])
    # dp[i][j] = minimum sum to reach cell (i, j)
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                # Starting cell
                dp[i][j] = grid[i][j]
                continue
            # Cost from above (if exists), else infinity
            up = dp[i - 1][j] if i > 0 else float("inf")
            # Cost from left (if exists), else infinity
            left = dp[i][j - 1] if j > 0 else float("inf")
            # Choose the minimum path
            dp[i][j] = grid[i][j] + min(up, left)

    return dp[-1][-1]


# Quick examples
print(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # Output: 7
print(minPathSum([[1, 2, 3], [4, 5, 6]]))  # Output: 12


def minPathSumInplace(grid):
    """Return minimum path sum using in-place modification.

    Modifies the grid in-place to avoid extra space.

    Args:
        grid (List[List[int]]): m x n grid of non-negative integers

    Returns:
        int: minimum sum along any path

    Complexity: Time O(m*n), Space O(1)
    """
    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                # Starting cell, no change
                continue
            # Cost from above (if exists), else infinity
            up = grid[i - 1][j] if i > 0 else float("inf")
            # Cost from left (if exists), else infinity
            left = grid[i][j - 1] if j > 0 else float("inf")
            # Update grid[i][j] with minimum path sum
            grid[i][j] += min(up, left)

    return grid[-1][-1]


print(minPathSumInplace([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # Output: 7
print(minPathSumInplace([[1, 2, 3], [4, 5, 6]]))  # Output: 12
