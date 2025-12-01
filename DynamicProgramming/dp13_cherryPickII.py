"""Cherry Pickup II.

Two robots start at top-left (0,0) and top-right (0,n-1) of an m x n grid.
Both move downward simultaneously. Each robot picks cherries (cell becomes
empty). When both visit the same cell, only one cherry is picked. Return
the maximum cherries collected by both robots reaching the bottom.

Movement: From (i,j) move to (i+1,j-1), (i+1,j), or (i+1,j+1).

Example 1:
    Grid: [[3,1,1],
           [2,5,1],
           [1,5,5],
           [2,1,1]]
    Robot1 path: (0,0)→(1,0)→(2,1)→(3,0) = 3+2+5+2 = 12
    Robot2 path: (0,2)→(1,1)→(2,2)→(3,2) = 1+5+5+1 = 12
    Total: 24

Example 2:
    Grid: [[1,0,0,0,0,0,1],
           [2,0,0,0,0,3,0],
           [2,0,9,0,0,0,0],
           [0,3,0,5,4,0,0],
           [1,0,2,3,0,0,6]]
    Maximum cherries: 28
"""

from typing import List


def cherryPickup(grid: List[List[int]]) -> int:
    """Return max cherries using memoized recursion.

    Two robots move simultaneously down the grid. Use recursion with
    memoization tracking both robots' column positions.

    Args:
        grid (List[List[int]]): m x n grid of cherry counts

    Returns:
        int: maximum cherries collected

    Complexity: Time O(m * n^2 * 9), Space O(m * n^2)
    """
    m, n = len(grid), len(grid[0])
    NEG = float("-inf")

    # dp[i][j1][j2] = max cherries from row i with robots at j1, j2
    dp = [[[NEG] * n for _ in range(n)] for _ in range(m)]

    def recursion(i, j1, j2):
        """Return max cherries from row i to bottom with robots at j1, j2."""
        # Out-of-bounds columns are invalid
        if j1 < 0 or j1 >= n or j2 < 0 or j2 >= n:
            return NEG

        # Return cached result if already computed
        if dp[i][j1][j2] != NEG:
            return dp[i][j1][j2]

        # last row
        if i == m - 1:
            if j1 == j2:
                dp[i][j1][j2] = grid[i][j1]
            else:
                dp[i][j1][j2] = grid[i][j1] + grid[i][j2]
            return dp[i][j1][j2]

        # recursive transitions
        maxi = NEG
        for dir1 in [-1, 0, 1]:
            for dir2 in [-1, 0, 1]:
                if j1 == j2:
                    cherries = grid[i][j1]
                else:
                    cherries = grid[i][j1] + grid[i][j2]

                cherries += recursion(i + 1, j1 + dir1, j2 + dir2)
                maxi = max(maxi, cherries)

        dp[i][j1][j2] = maxi
        return maxi

    return recursion(0, 0, n - 1)


# Outputs for testing
print(cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
# Output: 24
print(
    cherryPickup(
        [
            [1, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 3, 0],
            [2, 0, 9, 0, 0, 0, 0],
            [0, 3, 0, 5, 4, 0, 0],
            [1, 0, 2, 3, 0, 0, 6],
        ],
    )
)
# Output: 28


def cherryPickupDP(grid: List[List[int]]) -> int:
    """Return max cherries using bottom-up DP tabulation.

    Args:
        grid (List[List[int]]): m x n grid of cherry counts

    Returns:
        int: maximum cherries collected

    Complexity: Time O(m * n^2 * 9), Space O(m * n^2)
    """
    m, n = len(grid), len(grid[0])
    # Base case: last row, try all column pairs
    dp = [[[-1] * n for _ in range(n)] for _ in range(m)]
    for j1 in range(n):
        for j2 in range(n):
            if j1 == j2:
                dp[m - 1][j1][j2] = grid[m - 1][j1]
            else:
                dp[m - 1][j1][j2] = grid[m - 1][j1] + grid[m - 1][j2]
    for i in range(m - 2, -1, -1):
        for j1 in range(n):
            for j2 in range(n):
                max_cherries = -1
                for dir1 in range(-1, 2):
                    for dir2 in range(-1, 2):
                        if j1 == j2:
                            cherries = grid[i][j1]
                        else:
                            cherries = grid[i][j1] + grid[i][j2]
                        if 0 <= j1 + dir1 < n and 0 <= j2 + dir2 < n:
                            cherries += dp[i + 1][j1 + dir1][j2 + dir2]
                        else:
                            cherries += -1
                        max_cherries = max(max_cherries, cherries)
                dp[i][j1][j2] = max_cherries
    return dp[0][0][-1]


# Outputs for testing
print(cherryPickupDP([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
# Output: 24
print(
    cherryPickupDP(
        [
            [1, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 3, 0],
            [2, 0, 9, 0, 0, 0, 0],
            [0, 3, 0, 5, 4, 0, 0],
            [1, 0, 2, 3, 0, 0, 6],
        ],
    )
)
# Output: 28
