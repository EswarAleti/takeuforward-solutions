"""
Delete Operation for Two Strings
--------------------------------
LeetCode: https://leetcode.com/problems/delete-operation-for-two-strings/

Given two strings word1 and word2, return the minimum number of steps
required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Approach:
---------
The solution is based on the Longest Common Subsequence (LCS).

Let:
- m = len(word1)
- n = len(word2)
- lcs = length of LCS(word1, word2)

Characters belonging to the LCS are kept, and all others are deleted.

Minimum deletions required:
    (m - lcs) + (n - lcs) = m + n - 2 * lcs

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""


def minDistance(word1: str, word2: str) -> int:
    """
    Return the minimum number of delete operations required
    to make two strings identical.
    """

    m, n = len(word1), len(word2)

    # dp[i][j] stores the length of LCS between
    # word1[:i] and word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return m + n - 2 * dp[m][n]


# Test cases
if __name__ == "__main__":
    print(minDistance("sea", "eat"))  # Expected: 2
    print(minDistance("leetcode", "etco"))  # Expected: 4
    print(minDistance("abc", "abc"))  # Expected: 0
    print(minDistance("abc", "def"))  # Expected: 6
    print(minDistance("", "abc"))  # Expected: 3
    print(minDistance("abc", ""))  # Expected: 3
    print(minDistance("", ""))  # Expected: 0
