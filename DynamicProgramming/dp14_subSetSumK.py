"""
https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

Given an array of positive integers and a target sum, determine if a subset
exists with sum equal to the target.

Examples:
    arr = [3, 34, 4, 12, 5, 2], sum = 9 -> True
    arr = [3, 34, 4, 12, 5, 2], sum = 30 -> False
    arr = [1, 2, 3], sum = 6 -> True
"""


def isSubsetSumRecursion(arr, sum):
    """Check if subset with given sum exists using recursion.

    Args:
        arr (List[int]): array of positive integers
        sum (int): target sum to find

    Returns:
        bool: True if subset with sum exists, False otherwise

    Complexity: Time O(2^n), Space O(n) recursion stack
    """

    def recursion(i, target):
        """Return True if subset sum exists from index i with target."""
        # Base case: sum is 0, empty subset is valid
        if target == 0:
            return True
        if i < len(arr):
            # Skip current element
            skip = recursion(i + 1, target)
            # Include current element if possible
            include = recursion(i + 1, target - arr[i])
            return skip or include
        return False

    return recursion(0, sum)


# Quick examples
print(isSubsetSumRecursion([3, 34, 4, 12, 5, 2], 9))  # Output: True
print(isSubsetSumRecursion([3, 34, 4, 12, 5, 2], 30))  # Output: False
print(isSubsetSumRecursion([1, 2, 3], 6))  # Output: True


def isSubsetSumDP(arr, sum):
    """Check if subset with given sum exists using DP tabulation.

    dp[i][j] = True if subset of arr[0..i] with sum j exists.

    Args:
        arr (List[int]): array of positive integers
        sum (int): target sum to find

    Returns:
        bool: True if subset with sum exists, False otherwise

    Complexity: Time O(n*sum), Space O(n*sum)
    """
    n = len(arr)
    # dp[i][j] = can we make sum j using elements arr[0..i]
    dp = [[False] * (sum + 1) for _ in range(n)]

    # Base case: sum 0 is always possible (empty subset)
    for i in range(n):
        dp[i][0] = True

    # Fill the DP table
    for i in range(n):
        for j in range(1, sum + 1):
            # Option 1: don't include arr[i]
            dp[i][j] = dp[i - 1][j] if i > 0 else False
            # Option 2: include arr[i] if possible
            if arr[i] <= j:
                prev = dp[i - 1][j - arr[i]] if i > 0 else j == arr[i]
                dp[i][j] = dp[i][j] or prev

    return dp[-1][-1]


# Quick examples
print(isSubsetSumDP([3, 34, 4, 12, 5, 2], 9))  # Output: True
print(isSubsetSumDP([3, 34, 4, 12, 5, 2], 30))  # Output: False
print(isSubsetSumDP([1, 2, 3], 6))  # Output: True
