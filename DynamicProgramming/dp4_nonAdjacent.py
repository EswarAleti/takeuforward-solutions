"""
https://takeuforward.org/plus/dsa/problems/maximum-sum-of-non-adjacent-elements

Given an integer array nums of size n. Return the maximum sum possible
using elements of nums such that no two taken elements are adjacent.

This module provides two approaches:
- nonAdjacentSum: DP using a table of include/exclude values (O(n) time,
  O(n) space)
- nonAdjacentSumInplace: space-optimized DP using two variables (O(n) time,
  O(1) space)

Examples:
    nums = [1, 2, 4] -> 5
    nums = [2, 1, 4, 9] -> 11
"""


def nonAdjacentSum(nums):
    """Return max sum of non-adjacent elements using DP table.

    Args:
        nums (List[int]): input list of integers

    Returns:
        int: maximum non-adjacent sum

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    n = len(nums)
    # Empty list -> sum is 0
    if n == 0:
        return 0

    # dp[i] = [include_i, exclude_i]
    # include_i: max sum taking nums[i]
    # exclude_i: max sum not taking nums[i]
    dp = [[0, 0] for _ in range(n)]
    dp[0] = [nums[0], 0]

    for i in range(1, n):
        # If we include nums[i], we must have excluded i-1
        sum_include = nums[i] + dp[i - 1][1]
        # If we exclude nums[i], take the best of previous include/exclude
        sum_exclude = max(dp[i - 1][0], dp[i - 1][1])
        dp[i] = [sum_include, sum_exclude]

    # Answer is the best of including or excluding the last element
    return max(dp[-1][0], dp[-1][1])


# Quick examples / smoke tests
print(nonAdjacentSum([1, 2, 4]))  # Expected: 5
print(nonAdjacentSum([2, 1, 4, 9]))  # Expected: 11


def nonAdjacentSumInplace(nums):
    """Return max non-adjacent sum using O(1) extra space.

    Uses two variables to track best sums when including or
    excluding the previous element.

    Complexity:
        Time: O(n)
        Space: O(1)
    """
    n = len(nums)
    if n == 0:
        return 0

    # prev_incl: best sum that includes previous element
    # prev_excl: best sum that excludes previous element
    prev_incl = nums[0]
    prev_excl = 0

    for i in range(1, n):
        curr_incl = nums[i] + prev_excl
        curr_excl = max(prev_incl, prev_excl)

        # slide window for next iteration
        prev_incl = curr_incl
        prev_excl = curr_excl

    return max(prev_incl, prev_excl)


# Quick examples / smoke tests for inplace version
print(nonAdjacentSumInplace([1, 2, 4]))  # Expected: 5
print(nonAdjacentSumInplace([2, 1, 4, 9]))  # Expected: 11
