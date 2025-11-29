"""
https://takeuforward.org/plus/dsa/problems/ninja's-training

A ninja trains for n days. Each day he performs one of three activities:
running, stealth training, or fighting practice. The same activity cannot
be done on consecutive days. Each activity on each day yields merit points.

Given a n x 3-sized matrix, where matrix[i][0], matrix[i][1], and
matrix[i][2] represent the merit points for running, stealth, and fighting
practice on day i respectively. Return the maximum merit points earned.

Examples:
    matrix = [[10, 40, 70], [20, 50, 80], [30, 60, 90]] -> 210
    matrix = [[70, 40, 10], [180, 20, 5], [200, 60, 30]] -> 290
"""

from copy import deepcopy


def ninjaTraining(matrix):
    """Return max merit points the ninja can earn.

    Args:
        matrix (List[List[int]]): n x 3 matrix of points per day/activity

    Returns:
        int: maximum achievable merit points
    """
    dp = deepcopy(matrix)
    n_days, n_tasks = len(matrix), len(matrix[0])
    for day in range(1, n_days):
        for curr_task in range(n_tasks):
            for prev_task in range(n_tasks):
                if curr_task != prev_task:
                    dp[day][curr_task] = max(
                        dp[day][curr_task],
                        matrix[day][curr_task] + dp[day - 1][prev_task],
                    )
    return max(dp[-1])


# Quick examples / smoke tests
print(ninjaTraining([[10, 40, 70], [20, 50, 80], [30, 60, 90]]))  # Expected: 210
print(ninjaTraining([[70, 40, 10], [180, 20, 5], [200, 60, 30]]))  # Expected: 290
print(ninjaTraining([[1, 2, 5], [3, 1, 1], [3, 3, 3]]))  # Output: 11
print(ninjaTraining([[2, 1, 3], [3, 4, 6], [10, 1, 6], [8, 3, 7]]))  # Output: 25
print(ninjaTraining([[5, 10, 15]]))  # Output: 15
print(ninjaTraining([[50, 50, 50], [50, 50, 50], [50, 50, 50]]))  # Output: 150
print(ninjaTraining([[10, 100, 1], [1, 50, 1], [50, 1, 50]]))  # Output: 151
print(ninjaTraining([[1, 2, 3], [100, 1, 1], [1, 100, 1], [1, 1, 100]]))  # Output: 303
