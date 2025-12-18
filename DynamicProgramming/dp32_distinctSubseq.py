"""
Distinct Subsequences
---------------------
LeetCode: https://leetcode.com/problems/distinct-subsequences/

Given two strings ``s`` and ``t``, return the number of distinct subsequences
of ``s`` which equals ``t``.

A subsequence is formed by deleting zero or more characters without changing
order of the remaining characters.

The answer is guaranteed to fit within a 32-bit signed integer.

Examples:
---------
Input:  s = "rabbbit", t = "rabbit"
Output: 3

Input:  s = "babgbag", t = "bag"
Output: 5

This file contains two solutions:
1. Top-down recursion with memoization
2. Bottom-up dynamic programming

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""

from functools import lru_cache


def numDistinct(s: str, t: str) -> int:
    """
    Top-down recursive solution using memoization.
    """

    @lru_cache(None)
    def recursion(i: int, j: int) -> int:
        # All characters of t matched
        if j < 0:
            return 1
        # s exhausted but t still remains
        if i < 0:
            return 0

        if s[i] == t[j]:
            return recursion(i - 1, j) + recursion(i - 1, j - 1)
        return recursion(i - 1, j)

    return recursion(len(s) - 1, len(t) - 1)


# Quick examples
if __name__ == "__main__":
    print(numDistinct("rabbbit", "rabbit"))  # Expected: 3
    print(numDistinct("babgbag", "bag"))  # Expected: 5


def numDistinctDP(s: str, t: str) -> int:
    """
    Bottom-up dynamic programming solution.
    """

    m, n = len(s), len(t)

    # dp[i][j] = number of ways t[:j] can be formed from s[:i]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Empty t can be formed from any prefix of s
    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]

    return dp[m][n]


# Quick examples
if __name__ == "__main__":
    print(numDistinctDP("rabbbit", "rabbit"))  # Expected: 3
    print(numDistinctDP("babgbag", "bag"))  # Expected: 5


def numDistinctDP1D(s: str, t: str) -> int:
    """
    Space-optimized bottom-up dynamic programming solution.
    """
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        for j in range(n, 0, -1):
            if s[i - 1] == t[j - 1]:
                dp[j] += dp[j - 1]
    return dp[-1]


# Quick examples
if __name__ == "__main__":
    print(numDistinctDP1D("rabbbit", "rabbit"))  # Expected: 3
    print(numDistinctDP1D("babgbag", "bag"))  # Expected: 5
