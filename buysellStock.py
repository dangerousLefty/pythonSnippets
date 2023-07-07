def maxProfit(prices: list[int]) -> int:
    right = 1
    left = 0
    maxProfit = 0
    while right < len(prices) - 1:
        if prices[right] < prices[left]:
            left = right
            right += 1
        else:
            profit = prices[right] - prices[left]
            if profit > maxProfit:
                maxProfit = profit
            right += 1
    return maxProfit


myList = [7, 1, 5, 3, 6, 4]
j = maxProfit(myList)
print(j)
