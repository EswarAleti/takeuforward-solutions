"""
https://leetcode.com/problems/edit-distance/description/

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Input: word1 = "horse", word2 = "ros"
Output: 3

Input: word1 = "intention", word2 = "execution"
Output: 5
"""


def minDistanceRecursion(word1: str, word2: str) -> int:
    """Recursive solution for edit distance.

    Args:
        word1: Source string
        word2: Target string
    Returns:
        Minimum number of operations to convert word1 to word2
    Complexity:
        Time: Exponential in worst case
        Space: O(m + n) for recursion stack
    """

    def recursion(i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if word1[i] == word2[j]:
            return recursion(i - 1, j - 1)
        insert_op = 1 + recursion(i, j - 1)
        delete_op = 1 + recursion(i - 1, j)
        replace_op = 1 + recursion(i - 1, j - 1)
        return min(insert_op, delete_op, replace_op)

    return recursion(len(word1) - 1, len(word2) - 1)


# Examples
print(minDistanceRecursion("horse", "ros"))  # Output: 3
print(minDistanceRecursion("intention", "execution"))  # Output: 5


def minDistance2D(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for j in range(1, n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        dp[i][0] = i
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
    return dp[-1][-1]


# Examples
print(minDistance2D("horse", "ros"))  # Output: 3
print(minDistance2D("intention", "execution"))  # Output: 5
