"""
Print all longest common subsequences (LCS) in lexicographical order.

Given two strings, find and print all distinct longest common
subsequences sorted lexicographically. Uses DP table to store all
LCS possibilities at each step.

Example: s1 = "abaaa", s2 = "baabaca"
- LCS length = 4
- All LCS: "aaaa", "abaa", "baaa"
- Output: ["aaaa", "abaa", "baaa"] (sorted)
"""


def allLCS(s1, s2):
    """Find all distinct LCS in lexicographical order.

    Uses 3D DP where dp[i][j] stores list of all LCS from
    s1[0..i-1] and s2[0..j-1]. On character match, extend all
    previous LCS. On mismatch, take LCS from cell with greater
    length, or merge if equal.

    Args:
        s1: First string
        s2: Second string

    Returns:
        Sorted list of all distinct LCS

    Complexity:
        Time: O(m * n * k) where k = number of LCS and length
        Space: O(m * n * k) for storing all LCS strings
    """
    m, n = len(s1), len(s2)
    # DP table: dp[i][j] = list of all LCS from s1[0..i-1] and s2[0..j-1]
    dp = [[[""] for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = []
            # Characters match: extend all LCS from diagonal
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = [ss + s1[i - 1] for ss in dp[i - 1][j - 1]]
            else:
                # Characters don't match: compare LCS lengths
                len1 = len(dp[i - 1][j][0])
                len2 = len(dp[i][j - 1][0])
                # Take LCS from cell with greater length
                if len1 > len2:
                    dp[i][j] = dp[i - 1][j][:]
                elif len1 < len2:
                    dp[i][j] = dp[i][j - 1][:]
                else:
                    # Equal length: combine and remove duplicates
                    dp[i][j] = list(set(dp[i - 1][j] + dp[i][j - 1]))

    # Return sorted list of all distinct LCS
    return sorted(dp[-1][-1])


# Test cases
print(allLCS("abaaa", "baabaca"))  # Output: ['aaaa', 'abaa', 'baaa']
print(allLCS("aaa", "a"))  # Output: ['a']
print(allLCS("abaaa", "baabaa"))  # Output: ['aaaa', 'abaa', 'baaa']
