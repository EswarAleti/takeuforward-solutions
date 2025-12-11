"""
Target sum problem - count expressions with +/- signs achieving target.

Given array nums and target, assign +/- signs to each element and count
ways to reach target. This reduces to subset sum where:
- s1 (positive sum) - s2 (negative sum) = target
- s1 + s2 = total (sum of all elements)
- Solving: s1 = (total + target) / 2
- Count subsets with sum = s1

Example: nums = [1, 1, 1, 1, 1], target = 3
- Ways: +1+1+1-1-1, +1+1-1+1-1, +1-1+1+1-1, -1+1+1+1-1, +1+1+1+1-1
- Output: 5
"""

from typing import List


def findTargetSumWays(nums: List[int], target: int) -> int:
    """Target sum using pure recursion (exponential).

    For each element, try both +/- signs and count expressions that
    reach target. Base case: check if single element reaches target.

    Args:
        nums: List of integers
        target: Target sum to achieve

    Returns:
        Number of ways to reach target using +/- signs

    Complexity:
        Time: O(2^n), Space: O(n) recursion depth
    """

    def recursion(i, total):
        # Base case: only first element to process
        if i == 0:
            # Check if adding or subtracting first element reaches target
            pos_flag = (total + nums[i]) == target
            neg_flag = (total - nums[i]) == target
            return pos_flag + neg_flag

        # Try both + and - signs for current element
        pos_flag = recursion(i - 1, total + nums[i])
        neg_flag = recursion(i - 1, total - nums[i])
        return pos_flag + neg_flag

    n = len(nums)
    return recursion(n - 1, 0)


# Test cases for recursion approach
print(findTargetSumWays([1, 1, 1, 1, 1], 3))  # Output: 5
print(findTargetSumWays([1], 1))  # Output: 1
print(findTargetSumWays([2, 1], 1))  # Output: 1
print(findTargetSumWays([5, 2, 6, 4], 3))  # Output: 1


def findTargetSumWaysDP(nums: List[int], target: int) -> int:
    """Target sum using subset sum reduction (bottom-up DP).

    Reduces target sum to subset sum problem:
    - s1 - s2 = target, s1 + s2 = total
    - s1 = (total + target) / 2
    Count subsets with sum = s1 using 2D DP.

    Args:
        nums: List of integers
        target: Target sum to achieve

    Returns:
        Number of ways to reach target using +/- signs

    Complexity:
        Time: O(n * s1), Space: O(n * s1) where s1 = (total+target)/2
    """
    total = sum(nums)
    # Check if valid partition exists (must be non-negative and even)
    if (total - target) < 0 or (total - target) % 2 == 1:
        return 0

    # Calculate target subset sum
    tgt = (total - target) // 2
    n = len(nums)
    # DP table: dp[i][j] = count of ways to form sum j using nums[0..i]
    dp = [[0] * (tgt + 1) for _ in range(n)]

    # Base case: sum of 0 can be formed in 1 way (empty subset)
    for i in range(n):
        dp[i][0] = 1

    # Fill DP table using subset sum counting logic
    for i in range(n):
        for j in range(tgt + 1):
            # Don't include current element
            dp[i][j] = dp[i - 1][j]
            # Include current element if possible
            if nums[i] <= j:
                dp[i][j] += dp[i - 1][j - nums[i]]

    return dp[-1][-1]


# Test cases for DP approach
print(findTargetSumWaysDP([1, 1, 1, 1, 1], 3))  # Output: 5
print(findTargetSumWaysDP([1], 1))  # Output: 1
print(findTargetSumWaysDP([2, 1], 1))  # Output: 1
print(findTargetSumWaysDP([5, 2, 6, 4], 3))  # Output: 1
