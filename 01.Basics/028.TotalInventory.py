# Given a dictionary of item names and quantities, find the total number of items.
# Example: {"pens": 4, "books": 3, "erasers": 2} → 9

inventory = {"pens": 4, "books": 3, "erasers": 2}
total_items = 0

for val in inventory.values():
    total_items += val

print(total_items)