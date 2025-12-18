"""
Shortest Common Supersequence
-----------------------------
LeetCode: https://leetcode.com/problems/shortest-common-supersequence/

Given two strings ``str1`` and ``str2``, return the shortest string that has
both ``str1`` and ``str2`` as subsequences. If multiple answers exist,
return any one of them.

Approach:
---------
This solution first computes the **Longest Common Subsequence (LCS)** length
using dynamic programming. Then, it backtracks through the DP table to
construct the **Shortest Common Supersequence (SCS)**.

Key idea:
- When characters match, include the character once.
- When they differ, include the character from the string that gives a
  larger LCS value.
- Append remaining characters from either string once one is exhausted.

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""


def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    """
    Return the shortest common supersequence of two strings.
    """

    m, n = len(str1), len(str2)

    # dp[i][j] stores the length of LCS between
    # str1[:i] and str2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to build the result
    i, j = m, n
    result = ""

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            result += str1[i - 1]
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            result += str1[i - 1]
            i -= 1
        else:
            result += str2[j - 1]
            j -= 1

    # Append remaining characters
    while i > 0:
        result += str1[i - 1]
        i -= 1

    while j > 0:
        result += str2[j - 1]
        j -= 1

    return result[::-1]


# Test cases
if __name__ == "__main__":
    print(shortestCommonSupersequence(None, "abac", "cab"))  # cabac
    print(shortestCommonSupersequence(None, "abc", "xyz"))  # abcxyz
    print(shortestCommonSupersequence(None, "aggtab", "gxtxayb"))  # aggxtxayb
    print(shortestCommonSupersequence(None, "abcde", "ace"))  # abcede
    print(shortestCommonSupersequence(None, "abc", "abc"))  # abc
    print(shortestCommonSupersequence(None, "abc", "def"))  # abcdef
