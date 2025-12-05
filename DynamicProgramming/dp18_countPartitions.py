"""
https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1

Given an array arr[] and an integer diff, count the number of ways to
partition the array into two subsets such that the difference between
their sums is equal to diff.

Math:
- s1 + s2 = total (sum of both subsets equals total)
- s1 - s2 = diff (difference between subsets)
- Solving: s1 = (total + diff) / 2, s2 = (total - diff) / 2
- target = (total - diff) / 2
- If s1 (or target) is achievable, return count of ways to form it

Example: arr = [5, 2, 6, 4], diff = 3
- total = 17, target = (17 - 3) / 2 = 7
- s1 = 10, s2 = 7 (difference = 3)
- Output: 1 (one way to partition)
"""


def countPartitions(arr, diff):
    """Count partitions with given difference between subset sums.

    Math:
    - s1 + s2 = total (sum of both subsets equals total)
    - s1 - s2 = diff (difference between subsets)
    - Solving: s1 = (total + diff) / 2, s2 = (total - diff) / 2
    - target = (total - diff) / 2
    - If s1 (or target) is achievable, return count of ways

    Args:
        arr: List of integers
        diff: Target difference between two subset sums

    Returns:
        Number of ways to partition array with given difference
    """
    # Calculate total sum of array
    total = sum(arr)

    # Check if valid partition is possible
    # (total - diff) must be non-negative and even
    if total - diff < 0 or (total - diff) % 2:
        return 0

    # Calculate target sum using derived formula
    target = (total - diff) // 2
    n = len(arr)

    # DP table: dp[i][j] = count of ways to form sum j using arr[0..i]
    dp = [[0] * (target + 1) for _ in range(n)]

    # Base case: sum of 0 can be formed in 1 way (empty subset)
    for i in range(n):
        dp[i][0] = 1

    # Fill DP table using subset sum counting logic
    for i in range(n):
        for j in range(target + 1):
            # Don't include current element
            dp[i][j] = dp[i - 1][j]

            # Include current element if possible
            if j >= arr[i]:
                dp[i][j] += dp[i - 1][j - arr[i]]

    # Return count of ways to form target sum
    return dp[-1][-1]


# Quick examples
print(countPartitions([5, 2, 6, 4], 3))  # Output: 1
print(countPartitions([1, 1, 1, 1], 0))  # Output: 6
print(countPartitions([3, 2, 7, 1], 4))  # Output: 0
print(countPartitions([1, 2, 3, 4, 5], 3))  # Output: 3
