"""
https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1

Given an array of non-negative integers and a target sum, count all subsets
whose sum equals the target.

Examples:
    arr = [5, 2, 3, 10, 6, 8], target = 10 -> 3
    arr = [2, 5, 1, 4, 3], target = 10 -> 3
    arr = [35, 2, 8, 22], target = 0 -> 1
    arr = [35, 2, 8, 22, 0], target = 2 -> 2
"""


def perfectSumRecursion(arr, k):
    """Count subsets with given sum using recursion.

    Args:
        arr (List[int]): array of non-negative integers
        k (int): target sum

    Returns:
        int: number of subsets with sum = k

    Complexity: Time O(2^n), Space O(n) recursion stack
    """

    def recursion(i, target, arr):
        """Return count of subsets from arr[0..i] with target sum."""
        # Base case: processed all elements
        if i < 0:
            return 1 if target == 0 else 0

        # Option 1: don't include arr[i]
        not_take = recursion(i - 1, target, arr)

        # Option 2: include arr[i] if possible
        take = 0
        if arr[i] <= target:
            take = recursion(i - 1, target - arr[i], arr)

        return take + not_take

    return recursion(len(arr) - 1, k, arr)


# Quick examples
print(perfectSumRecursion([5, 2, 3, 10, 6, 8], 10))  # Output: 3
print(perfectSumRecursion([2, 5, 1, 4, 3], 10))  # Output: 3
print(perfectSumRecursion([5, 7, 8], 3))  # Output: 0
print(perfectSumRecursion([35, 2, 8, 22], 0))  # Output: 1
print(perfectSumRecursion([35, 2, 8, 22, 0], 2))  # Output: 2
print(perfectSumRecursion([28, 4, 3, 27, 0, 24, 26], 24))  # Output: 2


def perfectSumMemoization(arr, k):
    """Count subsets with given sum using memoized recursion.

    Args:
        arr (List[int]): array of non-negative integers
        k (int): target sum

    Returns:
        int: number of subsets with sum = k

    Complexity: Time O(n*k), Space O(n*k)
    """

    def recursion(i, target, arr, dp):
        """Return count of subsets from arr[0..i] with target sum."""
        # Base case: processed all elements
        if i < 0:
            return 1 if target == 0 else 0

        # Return cached result
        if dp[i][target] != -1:
            return dp[i][target]

        # Option 1: don't include arr[i]
        not_take = recursion(i - 1, target, arr, dp)

        # Option 2: include arr[i] if possible
        take = 0
        if arr[i] <= target:
            take = recursion(i - 1, target - arr[i], arr, dp)

        dp[i][target] = take + not_take
        return dp[i][target]

    dp = [[-1] * (k + 1) for _ in range(len(arr))]
    return recursion(len(arr) - 1, k, arr, dp)


# Quick examples
print(perfectSumMemoization([5, 2, 3, 10, 6, 8], 10))  # Output: 3
print(perfectSumMemoization([2, 5, 1, 4, 3], 10))  # Output: 3
print(perfectSumMemoization([5, 7, 8], 3))  # Output: 0
print(perfectSumMemoization([35, 2, 8, 22], 0))  # Output: 1
print(perfectSumMemoization([35, 2, 8, 22, 0], 2))  # Output: 2
print(perfectSumMemoization([28, 4, 3, 27, 0, 24, 26], 24))  # Output: 2


def perfectSum(arr, k):
    """Count subsets with given sum using bottom-up DP.

    Args:
        arr (List[int]): array of non-negative integers
        k (int): target sum

    Returns:
        int: number of subsets with sum = k

    Complexity: Time O(n*k), Space O(n*k)
    """
    n = len(arr)
    # dp[i][j] = count of subsets using arr[0..i] with sum j
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case: empty subset for sum 0
    for i in range(n):
        dp[i][0] = 1

    # Fill DP table
    for i in range(n):
        for j in range(k + 1):
            # Option 1: don't include arr[i]
            dp[i][j] = dp[i - 1][j] if i > 0 else (1 if j == 0 else 0)
            # Option 2: include arr[i] if possible
            if j >= arr[i]:
                dp[i][j] += (
                    dp[i - 1][j - arr[i]] if i > 0 else (1 if j == arr[i] else 0)
                )

    return dp[-1][-1]


# Quick examples
print(perfectSum([5, 2, 3, 10, 6, 8], 10))  # Output: 3
print(perfectSum([2, 5, 1, 4, 3], 10))  # Output: 3
print(perfectSum([5, 7, 8], 3))  # Output: 0
print(perfectSum([35, 2, 8, 22], 0))  # Output: 1
print(perfectSum([35, 2, 8, 22, 0], 2))  # Output: 2
print(perfectSum([28, 4, 3, 27, 0, 24, 26], 24))  # Output: 2
