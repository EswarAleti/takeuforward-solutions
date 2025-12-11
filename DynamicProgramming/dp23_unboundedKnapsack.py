"""
https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1

Given a set of items, each with a weight and a value, represented by the array wt[] and val[] respectively. Also, a knapsack with a weight limit capacity.
Your task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.

Note: Each item can be taken any number of times.

Input: val[] = [1, 1], wt[] = [2, 1], capacity = 3
Output: 3

Input: val[] = [10, 40, 50, 70], wt[] = [1, 3, 4, 5], capacity = 8
Output: 110

Input: val[] = [6, 8, 7, 100], wt[] = [2, 3, 4, 5], capacity = 1
Output: 0
"""


def knapSack2D(val, wt, capacity):
    n = len(val)
    dp = [[0] * (capacity + 1) for _ in range(n)]
    for i in range(n):
        for j in range(capacity + 1):
            dp[i][j] = dp[i - 1][j]
            if wt[i] <= j:
                dp[i][j] = max(dp[i][j], val[i] + dp[i][j - wt[i]])
    return dp[-1][-1]


# Test cases
print(knapSack2D([1, 1], [2, 1], 3))  # Output: 3
print(knapSack2D([10, 40, 50, 70], [1, 3, 4, 5], 8))  # Output: 110
print(knapSack2D([6, 8, 7, 100], [2, 3, 4, 5], 1))  # Output: 0


def knapSack1D(val, wt, capacity):
    n = len(val)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for j in range(capacity + 1):
            if wt[i] <= j:
                dp[j] = max(dp[j], val[i] + dp[j - wt[i]])
    return dp[-1]


# Test cases
print(knapSack1D([1, 1], [2, 1], 3))  # Output: 3
print(knapSack1D([10, 40, 50, 70], [1, 3, 4, 5], 8))  # Output: 110
print(knapSack1D([6, 8, 7, 100], [2, 3, 4, 5], 1))  # Output: 0
