def maxProfit(prices):
    # define var for min = maximum input
    minPrice = 10**4
    # define var for maxProfit =0 
    profitMax = 0
    # loop on prices
    for p in prices:
        # update min 
        if p < minPrice: minPrice = p
        # update profit
        if profitMax < p - minPrice:
            profitMax = p - minPrice
    
    return profitMax
