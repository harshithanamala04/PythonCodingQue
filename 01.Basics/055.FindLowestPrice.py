# Given a dictionary of items and prices, print the item with the lowest price. You may assume there is at least one item and no tied prices.
# Example: {"pen": 4, "book": 12, "eraser": 2} → eraser

def lowestPrice(stationary):
    lowest_item = None
    lowest_price = float('inf')

    for item,price in stationary.items():
        if price < lowest_price:
            lowest_price = price 
            lowest_item = item

    return lowest_item

stationary = {"pen": 4, "book": 12, "eraser": 2}

print(lowestPrice(stationary))