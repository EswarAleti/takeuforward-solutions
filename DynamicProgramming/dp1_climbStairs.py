# https://takeuforward.org/data-structure/dynamic-programming-climbing-stairs/
"""
Given an integer n, there is a staircase with n steps, starting from the 0th step.

Determine the number of unique ways to reach the nth step, given that each move can be either 1 or 2 steps at a time.

This module provides three solutions:
- climbStairsRecursion: naive recursion (exponential time)
- climbStairsTabulation: bottom-up DP using an array (O(n) time, O(n) space)
- climbStairsInplace: bottom-up DP using O(1) extra space (O(n) time, O(1) space)

Examples:

Input: n = 2
Output: 2

Input: n = 3
Output: 3

The problem is equivalent to computing the (n+1)th Fibonacci number when starting from 0 -> 1 -> 1 -> 2 -> ...
"""


def climbStairsRecursion(n):
    """Recursive solution.

    Args:
        n (int): target step index (non-negative)

    Returns:
        int: number of unique ways to reach step n using 1- or 2-step moves

    Notes:
        - This uses the recurrence ways(n) = ways(n-1) + ways(n-2).
        - Time complexity: O(2^n) in the worst case (exponential) due to repeated subproblems.
        - Space complexity: O(n) due to recursion stack.
    """
    # Base cases: if n is 0 or 1 there is exactly 1 way (stay or one single 1-step move)
    if n <= 1:
        return 1

    # Recur for previous two steps and sum their ways
    return climbStairsRecursion(n-1) + climbStairsRecursion(n-2)


print(climbStairsRecursion(2)) # Output: 2
print(climbStairsRecursion(3)) # Output: 3


def climbStairsTabulation(n):
    """Bottom-up dynamic programming (tabulation).

    Uses a DP array where dp[i] stores number of ways to reach step i.

    Args:
        n (int): target step index

    Returns:
        int: number of unique ways to reach step n

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    # Handle small n directly
    if n <= 1:
        return 1

    # dp[i] will hold the number of ways to reach step i
    dp = [0] * (n + 1)
    dp[0] = 1  # one way to be at step 0 (do nothing)
    dp[1] = 1  # one way to reach step 1 (one 1-step)

    # Fill the table from 2..n using the recurrence
    for i in range(2, n+1):
        # ways to reach i = ways to reach i-1 (then take 1 step)
        #                  + ways to reach i-2 (then take 2 steps)
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


print(climbStairsTabulation(2)) # Output: 2
print(climbStairsTabulation(3)) # Output: 3


def climbStairsInplace(n):
    """Space-optimized DP keeping only last two results.

    Instead of storing all dp values, we track only the last two counts (prev2 for i-2,
    prev1 for i-1) and compute the current number of ways.

    Args:
        n (int): target step index

    Returns:
        int: number of unique ways to reach step n

    Complexity:
        Time: O(n)
        Space: O(1)
    """
    # For n == 0 or n == 1 the answer is 1
    if n <= 1:
        return 1

    # Initialize prev2 = ways(0), prev1 = ways(1)
    prev2, prev1 = 1, 1

    # Iteratively compute ways(i) for i from 2 to n
    for i in range(2, n+1):
        ways = prev1 + prev2  # current ways based on previous two
        # shift window: prev2 becomes previous (i-1), prev1 becomes current (i)
        prev2 = prev1
        prev1 = ways

    # prev1 now holds ways(n)
    return prev1


print(climbStairsInplace(2)) # Output: 2
print(climbStairsInplace(3)) # Output: 3