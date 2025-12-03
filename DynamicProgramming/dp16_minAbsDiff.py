"""Partition Array into Two Subsets with Minimum Absolute Difference.

Given an array, partition it into two subsets such that the absolute
difference between their sums is minimized.

Examples:
    arr = [1, 7, 14, 5] -> 1 (partition: [1,7,5] and [14])
    arr = [3, 1, 6, 2, 2] -> 0 (partition: [3,2,2] and [6,1])
"""


def minDifference(arr, n):
    """Return minimum absolute difference when partitioning array.

    Approach: Find all possible subset sums using DP, then for each
    possible sum s1, compute s2 = total - s1 and track minimum difference.

    Args:
        arr (List[int]): array of integers
        n (int): length of array

    Returns:
        int: minimum absolute difference between two partition sums

    Complexity: Time O(n*sum), Space O(sum) where sum = sum(arr)
    """
    total = sum(arr)
    # dp[i] = True if sum i is achievable using subset of arr
    dp = [False] * (total + 1)
    dp[0] = True

    # Build all achievable subset sums
    for num in arr:
        # Traverse backwards to avoid reusing updated values
        for j in range(total, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    # Find partition with minimum difference
    min_diff = float("inf")
    for i in range(total // 2 + 1):
        # If both sum i and sum (total - i) are achievable
        if dp[i] and dp[total - i]:
            # Difference = |i - (total - i)| = |2*i - total|
            diff = abs(i - (total - i))
            min_diff = min(min_diff, diff)

    return min_diff


# Quick examples
print(minDifference([1, 7, 14, 5], 4))  # Output: 1
print(minDifference([3, 1, 6, 2, 2], 5))  # Output: 0
print(minDifference([1, 2, 3, 4, 5], 5))  # Output: 1
print(minDifference([10, 20, 15, 5, 25], 5))  # Output: 5
