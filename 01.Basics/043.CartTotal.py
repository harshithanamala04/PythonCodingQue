# Given a dictionary of item prices and a list of items in a cart, calculate the total cost. Items may appear more than once.
# Example: prices {"apple": 30, "bread": 25}, cart ["apple", "bread", "apple"] → 85

prices = {"apple": 30, "bread": 25}
cart = list(input("Enter items:").split())
total = 0

for item in cart:
    value = prices.get(item,0)
    total += value
print(total)