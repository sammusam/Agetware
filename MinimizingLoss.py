def minimize_loss(prices):
    indexed_prices = list(enumerate(prices))
    sorted_prices = sorted(indexed_prices, key=lambda x: x[1])
    min_loss = float('inf')
    buy_year = sell_year = -1

    for i in range(len(sorted_prices)-1, 0, -1):
        buy_idx, buy_price = sorted_prices[i]
        sell_idx, sell_price = sorted_prices[i-1]
        if buy_idx < sell_idx and buy_price > sell_price:
            loss = buy_price - sell_price
            if 0 < loss < min_loss:
                min_loss = loss
                buy_year, sell_year = buy_idx + 1, sell_idx + 1

    return (buy_year, sell_year, min_loss)

# Example:
print(minimize_loss([20, 15, 7, 2, 13]))  # (2, 5, 2)
