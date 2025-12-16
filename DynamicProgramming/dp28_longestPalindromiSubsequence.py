"""
Longest palindromic subsequence (LPS) - find length of LPS in string.

Given a string, find the length of its longest palindromic subsequence.
Reduces to finding LCS of string and its reverse: LCS(s, reverse(s))
represents the longest sequence that reads same forwards and backwards.

Example: s = "bbbab"
- Palindromic subsequences: "b", "bbb", "bbab", "bab"
- Longest: "bbab" with length 4
- Output: 4
"""


def longestPalindromeSubseq(s: str) -> int:
    """Longest palindromic subsequence using LCS reduction.

    Finds LCS of string and its reverse. A sequence that appears in
    both original and reversed string reads the same forwards and
    backwards (palindrome). Use standard LCS DP algorithm.

    Args:
        s: Input string

    Returns:
        Length of longest palindromic subsequence

    Complexity:
        Time: O(n^2), Space: O(n^2) where n = len(s)
    """
    # Original string and its reverse
    s1 = s
    s2 = s[::-1]
    n = len(s)
    # DP table: dp[i][j] = LCS length of s1[0..i-1] and s2[0..j-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill DP table using standard LCS logic
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Characters match: include in LCS
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # Characters don't match: take max from left or top
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS of string and reverse = longest palindromic subsequence
    return dp[-1][-1]


# Test cases
print(longestPalindromeSubseq("bbbab"))  # Output: 4
print(longestPalindromeSubseq("cbbd"))  # Output: 2
print(longestPalindromeSubseq("agbdba"))  # Output: 5
print(longestPalindromeSubseq("abcd"))  # Output: 1
