"""
https://takeuforward.org/plus/dsa/problems/house-robber

Circular House Robber problem: houses are arranged in a circle. Each house
has some amount of money. Robbing two adjacent houses triggers the alarm.

Given a list `money`, where `money[i]` is the loot in the i-th house,
return the maximum money that can be looted without robbing two adjacent
houses. Because the houses are circular, the first and last houses are
considered adjacent.

Examples:
    money = [2, 1, 4, 9] -> 10
    money = [1, 5, 2, 1, 6] -> 11
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


def houseRobber(nums):
    """Maximum loot for circular street of houses.

    Approach:
    - If there are no houses return 0.
    - If there is only one house return its value.
    - For n >= 2, the circular condition can be handled by considering two
      linear cases and taking the maximum:
        1) Rob houses in range [1..n-1] (exclude first house)
        2) Rob houses in range [0..n-2] (exclude last house)

    This reduces the circular problem to two standard linear house-robber
    problems solved by `nonAdjacentSum`.
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    # Compute both scenarios and return the best
    return max(nonAdjacentSum(nums[1:]), nonAdjacentSum(nums[:-1]))


# Quick examples / smoke tests
print(houseRobber([2, 1, 4, 9]))  # Expected: 10
print(houseRobber([1, 5, 2, 1, 6]))  # Expected: 11
