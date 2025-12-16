"""
Longest common substring (LCS) - find length of longest common substring.

Given two strings, find the length of their longest common substring.
A substring is contiguous (unlike subsequence which can skip chars).

Example: s1 = "ABCDGH", s2 = "ACDGHR"
- Common substrings: "A", "CD", "DG", "GH", "HR"
- Longest: "CDGH" with length 4
- Output: 4
"""


def longestCommonSubstr(s1, s2):
    """Longest common substring using DP.

    Uses 2D DP where dp[i][j] = length of common substring ending at
    s1[i-1] and s2[j-1]. When characters match, extend from diagonal.
    When they don't, reset to 0 (substring must be contiguous).

    Args:
        s1: First string
        s2: Second string

    Returns:
        Length of longest common substring

    Complexity:
        Time: O(m * n), Space: O(m * n) where m, n = string lengths
    """
    m, n = len(s1), len(s2)
    # DP table: dp[i][j] = length of common substring ending at
    # s1[i-1] and s2[j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Characters match: extend substring from diagonal
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                # Update max length
                max_len = max(max_len, dp[i][j])

    return max_len


# Test cases
print(longestCommonSubstr("ABCDGH", "ACDGHR"))  # Output: 4
print(longestCommonSubstr("abc", "acb"))  # Output: 1
print(longestCommonSubstr("YZ", "yz"))  # Output: 0
