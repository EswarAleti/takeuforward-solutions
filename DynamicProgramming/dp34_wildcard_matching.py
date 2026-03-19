"""
Wildcard pattern matching - support '?' and '*' wildcards.

Given a string and a pattern, implement wildcard matching where:
- '?' matches any single character
- '*' matches any sequence of characters (including empty sequence)
The matching must cover the entire string.

Example: s = "adceb", p = "*a*b"
- '*' matches "" (empty), 'a' matches 'a', '*' matches "dce", 'b' matches 'b'
- Output: true
"""


def isMatch(s: str, p: str) -> bool:
    """Wildcard matching using pure recursion (exponential).

    Try all three cases for each character: exact match, '?' matches single char,
    or '*' matches zero or more characters.

    Args:
        s: Input string to match
        p: Pattern with '?' and '*' wildcards
    Returns:
        True if entire string matches pattern, False otherwise
    Complexity:
        Time: Exponential in worst case
        Space: O(m + n) for recursion stack
    """

    def recursion(i, j):
        # Both string and pattern exhausted - match found
        if i < 0 and j < 0:
            return True
        # String exhausted but pattern remains - only match if all remaining are '*'
        if i < 0:
            return p[: j + 1].count("*") == j + 1
        # Pattern exhausted but string remains - no match
        if j < 0:
            return False
        # Exact match or '?' matches any single character
        if s[i] == p[j] or p[j] == "?":
            return recursion(i - 1, j - 1)
        # '*' can match zero chars (skip '*') or one/more chars (skip from string)
        if p[j] == "*":
            return recursion(i, j - 1) or recursion(i - 1, j)
        return False

    return recursion(len(s) - 1, len(p) - 1)


# Test cases for recursion approach
print(isMatch("aa", "a"))  # Output: False
print(isMatch("aa", "*"))  # Output: True
print(isMatch("cb", "?a"))  # Output: False
print(isMatch("adceb", "*a*b"))  # Output: True
print(isMatch("acdcb", "a*c?b"))  # Output: False
print(isMatch("", "***"))  # Output: True


def isMatchMemoization(s: str, p: str) -> bool:
    """Wildcard matching using memoized recursion (top-down DP).

    Cache results of overlapping subproblems to avoid redundant computation.
    dp[i][j] = cached result for matching s[0..i] with p[0..j].

    Args:
        s: Input string to match
        p: Pattern with '?' and '*' wildcards
    Returns:
        True if entire string matches pattern, False otherwise
    Complexity:
        Time: O(m * n), Space: O(m * n) for DP cache
    """
    dp = [[-1] * (len(p) + 1) for _ in range(len(s) + 1)]

    def recursion(i, j):
        # Both exhausted - match found
        if i < 0 and j < 0:
            return True
        # Pattern exhausted but string remains - only match if all remaining are '*'
        if i < 0:
            return j == p[: j + 1].count("*") - 1
        # String exhausted but pattern remains - no match
        if j < 0:
            return False
        # Return cached result if available
        if dp[i][j] != -1:
            return dp[i][j]
        # Exact match or '?' matches any single character
        if s[i] == p[j] or p[j] == "?":
            dp[i][j] = recursion(i - 1, j - 1)
            return dp[i][j]
        # '*' can match zero chars (skip '*') or one/more chars (skip from string)
        if p[j] == "*":
            dp[i][j] = recursion(i, j - 1) or recursion(i - 1, j)
            return dp[i][j]
        # No match for this character combination
        dp[i][j] = False
        return dp[i][j]

    return recursion(len(s) - 1, len(p) - 1)


# Test cases for memoization approach
print(isMatchMemoization("aa", "a"))  # Output: False
print(isMatchMemoization("aa", "*"))  # Output: True
print(isMatchMemoization("cb", "?a"))  # Output: False
print(isMatchMemoization("adceb", "*a*b"))  # Output: True
print(isMatchMemoization("acdcb", "a*c?b"))  # Output: False
print(isMatchMemoization("", "***"))  # Output: True


def isMatchDP(s: str, p: str) -> bool:
    """Wildcard matching using bottom-up DP.

    Build DP table where dp[i][j] represents if s[0..i-1] matches p[0..j-1].
    Base case: empty string and empty pattern match.
    Fill by considering character matches and wildcard behaviors.

    Args:
        s: Input string to match
        p: Pattern with '?' and '*' wildcards
    Returns:
        True if entire string matches pattern, False otherwise
    Complexity:
        Time: O(m * n), Space: O(m * n)
    """
    m, n = len(s), len(p)
    # dp[i][j] = True if s[0..i-1] matches p[0..j-1]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    # Base: empty string and empty pattern match
    dp[0][0] = True
    # Handle patterns like "*", "**", etc. that can match empty string
    for j in range(1, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                # Character match or '?' wildcard
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == "*":
                # '*' can match zero chars (dp[i][j-1]) or one/more chars (dp[i-1][j])
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[-1][-1]


# Test cases for DP approach
print(isMatchDP("aa", "a"))  # Output: False
print(isMatchDP("aa", "*"))  # Output: True
print(isMatchDP("cb", "?a"))  # Output: False
print(isMatchDP("adceb", "*a*b"))  # Output: True
print(isMatchDP("acdcb", "a*c?b"))  # Output: False
print(isMatchDP("", "***"))  # Output: True
