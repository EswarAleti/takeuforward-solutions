"""Unique Paths in Grid with Obstacles.

Given an m x n grid where 0=open and 1=blocked, return the number of
unique paths from top-left (0,0) to bottom-right (m-1,n-1). Movement
is only right or down.

Examples:
    grid = [[0,0,0],[0,1,0],[0,0,0]] -> 2
    grid = [[0,0,0],[0,0,1],[0,1,0]] -> 0
"""


def uniquePathsWithObstacles(obstacleGrid):
    """Return unique paths in grid with obstacles using DP table.

    Args:
        obstacleGrid (List[List[int]]): m x n grid (0=open, 1=blocked)

    Returns:
        int: number of unique paths

    Complexity: Time O(m*n), Space O(m*n)
    """
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    # dp[i][j] = number of ways to reach cell (i, j)
    dp = [[0] * n for _ in range(m)]

    for i in range(0, m):
        for j in range(0, n):
            if obstacleGrid[i][j]:
                # Blocked cell, no paths through it
                dp[i][j] = 0
            elif i == 0 and j == 0:
                # Starting cell
                dp[i][j] = 1
            else:
                # Sum paths from top and left
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
# Output: 2
print(uniquePathsWithObstacles([[0, 0, 0], [0, 0, 1], [0, 1, 0]]))
# Output: 0


def uniquePathsWithObstaclesInplace(obstacleGrid):
    """Return unique paths using space-optimized DP (O(n) space).

    Args:
        obstacleGrid (List[List[int]]): m x n grid (0=open, 1=blocked)

    Returns:
        int: number of unique paths

    Complexity: Time O(m*n), Space O(n)
    """
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * n

    for i in range(0, m):
        curr = [0] * n
        for j in range(0, n):
            if obstacleGrid[i][j]:
                # Blocked cell
                curr[j] = 0
            elif i == 0 and j == 0:
                # Starting cell
                curr[j] = 1
            else:
                # Sum from above (dp[j]) and from left (curr[j-1])
                curr[j] = dp[j] + curr[j - 1]
        dp = curr
    return dp[-1]


print(uniquePathsWithObstaclesInplace([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
# Output: 2
print(uniquePathsWithObstaclesInplace([[0, 0, 0], [0, 0, 1], [0, 1, 0]]))
# Output: 0
