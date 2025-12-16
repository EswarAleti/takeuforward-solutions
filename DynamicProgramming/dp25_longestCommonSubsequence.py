"""
Longest common subsequence (LCS) - find length of common subsequence.

Given two strings, find the length of their longest common subsequence.
A subsequence maintains relative order but may skip characters.

Example: text1 = "abcde", text2 = "ace"
- Subsequences of "abcde": "a", "ae", "ace", "bcde", ...
- Common: "a", "ae", "ace", ...
- LCS: "ace" with length 3
- Output: 3
"""


def longestCommonSubsequence(text1: str, text2: str) -> int:
    """LCS using pure recursion (exponential).

    For each character pair, if match found, take 1 and recurse on
    remaining. If no match, try skipping from either string (max of
    two options).

    Args:
        text1: First string
        text2: Second string

    Returns:
        Length of longest common subsequence

    Complexity:
        Time: O(2^(m+n)), Space: O(m+n) recursion depth
    """

    def recursion(i, j):
        # Base case: one string exhausted
        if i < 0 or j < 0:
            return 0

        # Characters match: include in LCS
        if text1[i] == text2[j]:
            return 1 + recursion(i - 1, j - 1)

        # Characters don't match: try skipping from either string
        return max(recursion(i - 1, j), recursion(i, j - 1))

    return recursion(len(text1) - 1, len(text2) - 1)


# Test cases for recursion approach
print(longestCommonSubsequence("abcde", "ace"))  # Output: 3
print(longestCommonSubsequence("abc", "abc"))  # Output: 3
print(longestCommonSubsequence("abc", "def"))  # Output: 0


def longestCommonSubsequenceDP(text1: str, text2: str) -> int:
    """LCS using bottom-up DP.

    Uses 2D DP where dp[i][j] = LCS length of text1[0..i-1] and
    text2[0..j-1]. If characters match, take diagonal value + 1.
    Otherwise, take max from left or top.

    Args:
        text1: First string
        text2: Second string

    Returns:
        Length of longest common subsequence

    Complexity:
        Time: O(m * n), Space: O(m * n) where m, n = string lengths
    """
    m, n = len(text1), len(text2)
    # DP table: dp[i][j] = LCS length of text1[0..i-1] and text2[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Characters match: take diagonal + 1
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # Characters don't match: take max from left or top
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


# Test cases for DP approach
print(longestCommonSubsequenceDP("abcde", "ace"))  # Output: 3
print(longestCommonSubsequenceDP("abc", "abc"))  # Output: 3
print(longestCommonSubsequenceDP("abc", "def"))  # Output: 0
