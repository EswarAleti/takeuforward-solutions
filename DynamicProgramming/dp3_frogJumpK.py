"""
https://takeuforward.org/data-structure/dynamic-programming-frog-jump-with-k-
distances-dp-4/

A frog wants to climb a staircase with n steps. Given an integer array
heights, where heights[i] contains the height of the ith step, and an
integer k.

To jump from the ith step to the jth step, the frog requires
abs(heights[i] - heights[j]) energy, where abs() denotes the absolute
difference. The frog can jump from the ith step to any step in the range
[i + 1, i + k], provided it exists.

Return the minimum amount of energy required by the frog to go from the
0th step to the (n-1)th step.

Examples:

Input: heights = [10, 5, 20, 0, 15], k = 2
Output: 15
Explanation:
0th step -> 2nd step, cost = abs(10 - 20) = 10
2nd step -> 4th step, cost = abs(20 - 15) = 5
Total cost = 10 + 5 = 15.

Input: heights = [15, 4, 1, 14, 15], k = 3
Output: 2
Explanation:
0th step -> 3rd step, cost = abs(15 - 14) = 1
3rd step -> 4th step, cost = abs(14 - 15) = 1
Total cost = 1 + 1 = 2.
"""


def frogJumpK(heights, k):
    """Minimum energy to reach last step when frog can jump up to k steps.

    Args:
        heights (List[int]): heights of the steps
        k (int): maximum number of steps the frog can jump in one move

    Returns:
        int: minimum energy required to reach the last step (index n-1)

    Complexity:
        Time: O(n * k) — for each of n steps we consider up to k previous
        jumps
        Space: O(n) for the dp array
    """
    n = len(heights)
    # If only one step, no energy is required
    if n == 1:
        return 0

    # dp[i] stores the minimum energy to reach step i
    # Initialize with +inf so that min comparisons work correctly
    dp = [float("inf")] * n
    dp[0] = 0

    # For every step i, check all possible previous steps j from which
    # the frog could have jumped (within k distance) and pick the best
    for i in range(1, n):
        # j ranges from i-k up to i-1 (bounded by 0)
        for j in range(max(0, i - k), i):
            dp[i] = min(dp[i], dp[j] + abs(heights[i] - heights[j]))

    return dp[-1]


# Quick examples / smoke tests
# The prints below demonstrate expected outputs for simple inputs.
print(frogJumpK([10, 5, 20, 0, 15], 2))  # Expected: 15
print(frogJumpK([15, 4, 1, 14, 15], 3))  # Expected: 2
