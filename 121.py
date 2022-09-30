def maxProfit(prices: list[int]) -> int:
    # max_prof = 0
    # left = 0
    # right = 1
    # while right < len(prices):
    #     curr_prof = prices[right] - prices[left]
    #     if prices[left] < prices[right]:
    #         max_prof = max(curr_prof, max_prof)
    #     else:
    #         left = right
    #     right += 1
    # return max_prof

    max_prof = 0
    min_val = prices[0]
    for price in prices:
        cur_prof = price - min_val
        if cur_prof > max_prof:
            max_prof = cur_prof
        if price < min_val:
            min_val = price
    return max_prof

print(maxProfit([7,1,5,3,6,4]))