"""
Minimum insertions to make palindrome - find min chars to insert.

Given a string, find the minimum number of character insertions
needed to make it a palindrome. Uses LPS (Longest Palindromic
Subsequence): min insertions = length - LPS(string).

Example: s = "leetcode"
- LPS length = 3 ("ete" or "tee")
- Need to insert: 8 - 3 = 5 characters
- Output: 5
"""


def minInsertions(s: str) -> int:
    """Minimum insertions to make palindrome using LPS reduction.

    Finds LPS (Longest Palindromic Subsequence) length. Characters
    not in LPS must be inserted (1 insertion = 1 character not in LPS).
    Formula: min insertions = length - LPS_length

    Args:
        s: Input string

    Returns:
        Minimum number of insertions needed to make palindrome

    Complexity:
        Time: O(n^2), Space: O(n^2) where n = len(s)
    """
    # Find LCS of string and its reverse (= LPS length)
    s1, s2 = s, s[::-1]
    n = len(s1)
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

    # Chars to insert = total length - LPS length
    return n - dp[-1][-1]


# Test cases
print(minInsertions("zzazz"))  # Output: 0
print(minInsertions("mbadm"))  # Output: 2
print(minInsertions("leetcode"))  # Output: 5
