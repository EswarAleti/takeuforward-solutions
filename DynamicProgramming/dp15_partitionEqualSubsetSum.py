"""Partition Equal Subset Sum.

https://leetcode.com/problems/partition-equal-subset-sum/description/

Given an integer array, partition it into two subsets with equal sum.
Return True if such a partition exists, False otherwise.

Examples:
    nums = [1, 5, 11, 5] -> True (subsets: {11} and {5,5,1})
    nums = [1, 2, 3, 5] -> False
"""

from typing import List


def isSubsetSum(nums: List[int], target: int) -> bool:
    """Check if a subset with given target sum exists.

    Args:
        nums (List[int]): array of integers
        target (int): target sum to find

    Returns:
        bool: True if subset with sum=target exists

    Complexity: Time O(n*target), Space O(n*target)
    """
    n = len(nums)
    # dp[i][j] = can we make sum j using nums[0..i]
    dp = [[False] * (target + 1) for _ in range(n)]

    for i in range(n):
        for j in range(target + 1):
            # Base case: sum 0 is always achievable
            if j == 0:
                dp[i][j] = True
                continue
            # Option 1: don't include nums[i]
            dp[i][j] = dp[i - 1][j] if i > 0 else False
            # Option 2: include nums[i] if possible
            if nums[i] <= j:
                prev = dp[i - 1][j - nums[i]] if i > 0 else j == nums[i]
                dp[i][j] = dp[i][j] or prev
    return dp[-1][-1]


def canPartition(nums: List[int]) -> bool:
    """Check if array can be partitioned into two equal-sum subsets.

    Approach: If total sum is odd, partition is impossible. Otherwise,
    reduce to subset sum problem: check if a subset with sum = total/2
    exists using dynamic programming.

    Args:
        nums (List[int]): array of integers

    Returns:
        bool: True if partition exists

    Complexity: Time O(n*sum), Space O(n*sum) where sum = sum(nums)
    """
    total = sum(nums)
    # Odd sum cannot be partitioned into two equal subsets
    if total % 2 == 1:
        return False
    # Reduce to subset sum: find subset with sum = total // 2
    return isSubsetSum(nums, total // 2)


# Quick examples
print(canPartition([1, 5, 11, 5]))  # Output: True
print(canPartition([1, 2, 3, 5]))  # Output: False
