"""
Best time to buy and sell stock (one transaction).

Given stock prices for each day, find the maximum profit from buying once and selling once.
You must buy before you sell, and you can only make one transaction.

Example: prices = [7, 1, 5, 3, 6, 4]
- Buy at 1, sell at 6 for profit = 5
- Output: 5
"""


def maxProfit(prices: list[int]) -> int:
    """Maximum profit from single buy-sell transaction.

    Track the minimum price seen so far and at each price, compute the profit
    if we sold at that price. Return the maximum profit found.

    Args:
        prices: List of integers representing stock prices per day
    Returns:
        Maximum profit from one buy-sell transaction, or 0 if no profit possible
    Complexity:
        Time: O(n), Space: O(1)
    """
    min_price = float("inf")
    profit = 0
    # Track minimum price and maximum profit as we iterate
    for price in prices:
        min_price = min(min_price, price)
        # Profit if we sell at current price
        profit = max(profit, price - min_price)
    return profit


# Test cases for buy-sell stock (one transaction)
print(maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5 (buy at 1, sell at 6)
print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0 (no profit possible)
