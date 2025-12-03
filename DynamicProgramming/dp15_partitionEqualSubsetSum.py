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
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: sum 0 is always achievable
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]


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


def canPartitionInplace(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: sum 0 is always achievable

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]


# Quick examples
print(canPartitionInplace([1, 5, 11, 5]))  # Output: True
print(canPartitionInplace([1, 2, 3, 5]))  # Output: False
