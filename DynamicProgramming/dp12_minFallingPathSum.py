"""Minimum Falling Path Sum in Matrix.

Given an n x n matrix, return minimum sum of any falling path. A falling
path starts at any element in row 0 and moves to row below, either directly
below or diagonally (left/right).

Examples:
    matrix = [[2,1,3],[6,5,4],[7,8,9]] -> 13
    matrix = [[-19,57],[-40,-5]] -> -59
"""


def minFallingPath(matrix):
    """Return minimum falling path sum using space-optimized DP.

    Args:
        matrix (List[List[int]]): n x n matrix of integers

    Returns:
        int: minimum sum of any falling path

    Complexity: Time O(n^2), Space O(n)
    """
    dp = matrix[0]
    m, n = len(matrix), len(matrix[0])

    for i in range(1, m):
        curr = matrix[i]
        for j in range(n):
            # Three options from previous row: left-diag, top, right-diag
            left_diag = dp[j - 1] if j > 0 else float("inf")
            top = dp[j]
            right_diag = dp[j + 1] if j + 1 < n else float("inf")
            # Update current with minimum path sum
            curr[j] = matrix[i][j] + min(left_diag, top, right_diag)
        dp = curr

    return min(dp)


# Quick examples
print(minFallingPath([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))  # Output: 13
print(minFallingPath([[-19, 57], [-40, -5]]))  # Output: -59


def minFallingPathSumInplace(matrix):
    """Return minimum falling path sum using in-place modification.

    Args:
        matrix (List[List[int]]): n x n matrix of integers

    Returns:
        int: minimum sum of any falling path

    Complexity: Time O(n^2), Space O(1) (modifies input)
    """
    m, n = len(matrix), len(matrix[0])

    for i in range(1, m):
        for j in range(n):
            # Three options: left-diag, top, right-diag from previous row
            left_diag = matrix[i - 1][j - 1] if j > 0 else float("inf")
            top = matrix[i - 1][j]
            right_diag = matrix[i - 1][j + 1] if j + 1 < n else float("inf")
            # Update with minimum path sum
            matrix[i][j] += min(left_diag, top, right_diag)

    return min(matrix[-1])


# Quick examples
print(minFallingPathSumInplace([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
# Output: 13
print(minFallingPathSumInplace([[-19, 57], [-40, -5]]))  # Output: -59
