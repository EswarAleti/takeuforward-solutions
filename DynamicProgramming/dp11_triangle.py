"""Minimum Path Sum in Triangle.

Given a triangle array, return minimum path sum from top to bottom.
Each step moves to an adjacent number in the row below (index i or i+1).

Examples:
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]] -> 11
    triangle = [[-10]] -> -10
"""


def minimumTotal(triangle):
    """Return minimum path sum in triangle using space-optimized DP.

    Args:
        triangle (List[List[int]]): triangle of integers

    Returns:
        int: minimum sum from top to bottom

    Complexity: Time O(n^2), Space O(n) where n is triangle height
    """
    # Start with the top element
    dp = [triangle[0][0]]

    # Process each row
    for i in range(1, len(triangle)):
        curr = []
        for j in range(len(triangle[i])):
            # Option 1: from position j in previous row
            up = dp[j] if j < len(dp) else float("inf")
            # Option 2: from position j-1 in previous row
            corner = dp[j - 1] if j > 0 else float("inf")
            # Take minimum and add current element
            curr.append(triangle[i][j] + min(up, corner))
        dp = curr

    # Return minimum in the last row
    return min(dp)


# Quick examples
print(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
# Output: 11
print(minimumTotal([[-10]]))  # Output: -10


def miniumTotalInplace(triangle):
    """Return minimum path sum in triangle using in-place modification.

    Args:
        triangle (List[List[int]]): triangle of integers

    Returns:
        int: minimum sum from top to bottom

    Complexity: Time O(n^2), Space O(1) (modifies input)
    """
    # Process each row starting from second
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # Option 1: from position j in previous row
            up = triangle[i - 1][j] if j < len(triangle[i - 1]) else float("inf")
            # Option 2: from position j-1 in previous row
            corner = triangle[i - 1][j - 1] if j > 0 else float("inf")
            # Update with minimum path sum
            triangle[i][j] += min(up, corner)

    return min(triangle[-1])


# Quick examples
print(miniumTotalInplace([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
# Output: 11
print(miniumTotalInplace([[-10]]))  # Output: -10
