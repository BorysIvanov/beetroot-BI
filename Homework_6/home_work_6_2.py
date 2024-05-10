stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_prices = {}

for item, quantity in stock.items():
    total_price = prices[item] * quantity
    total_prices[item] = total_price
print("Total prices:", total_prices)
