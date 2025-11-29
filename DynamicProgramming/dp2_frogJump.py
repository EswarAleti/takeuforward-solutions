"""
https://takeuforward.org/data-structure/dynamic-programming-frog-jump-dp-3/

A frog wants to climb a staircase with n steps. Given an integer array heights, where heights[i]
contains the height of the ith step.

To jump from the ith step to the jth step, the frog requires abs(heights[i] - heights[j]) energy.
The frog can jump either one or two steps at a time.

This module provides two implementations:
- frogJump: DP using an array (O(n) time, O(n) space)
- frogJumpInplace: space-optimized DP using two variables (O(n) time, O(1) space)
"""


def frogJump(n, heights):
    """Compute minimum energy to reach the last step using a DP array.

    Args:
        n (int): number of steps (len(heights))
        heights (List[int]): heights of each step

    Returns:
        int: minimum energy to reach step n-1

    Complexity: Time O(n), Space O(n)
    """
    # If only one step, no energy is needed
    if len(heights) == 1:
        return 0

    # dp[i] = minimum energy to reach step i
    dp = [0] * n
    dp[0] = 0
    # base case for the first jump
    dp[1] = abs(heights[1] - heights[0])

    # Build dp table using recurrence:
    # dp[i] = min(dp[i-1] + cost(i-1->i), dp[i-2] + cost(i-2->i))
    for i in range(2, n):
        cost_from_prev = dp[i - 1] + abs(heights[i] - heights[i - 1])
        cost_from_prev2 = dp[i - 2] + abs(heights[i] - heights[i - 2])
        dp[i] = min(cost_from_prev, cost_from_prev2)

    return dp[-1]


# Quick examples
print(frogJump(5, [2, 1, 3, 5, 4]))  # Output: 2
print(frogJump(5, [7, 5, 1, 2, 6]))  # Output: 9


def frogJumpInplace(n, heights):
    """Space-optimized DP keeping only last two states.

    Args and return as in frogJump.

    Complexity: Time O(n), Space O(1)
    """
    if len(heights) == 1:
        return 0

    # prev2 = dp[i-2], prev1 = dp[i-1]
    prev2 = 0
    prev1 = abs(heights[1] - heights[0])

    # Iterate and compute current minimum using only prev1 and prev2
    for i in range(2, n):
        cost_from_prev = prev1 + abs(heights[i] - heights[i - 1])
        cost_from_prev2 = prev2 + abs(heights[i] - heights[i - 2])
        curr = min(cost_from_prev, cost_from_prev2)

        # slide the window
        prev2 = prev1
        prev1 = curr

    return prev1


# Same examples for the inplace version
print(frogJumpInplace(5, [2, 1, 3, 5, 4]))  # Output: 2
print(frogJumpInplace(5, [7, 5, 1, 2, 6]))  # Output: 9
