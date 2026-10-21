# Given a dictionary of item quantities, ask for an item and an amount to add. Update that item’s quantity, or add it if it isn’t already in the dictionary.
# Example: {"pens": 4, "books": 3}, add 2 to "pens" → {"pens": 6, "books": 3}

inventory = {"pens": 4, "books": 3}
n = int(input("Enter how many items u want to add:"))

for _ in range(n):
    key = input("Enter Key:").lower()
    val = int(input(f"Enter value for the {key}:"))

    if key in inventory:
        inventory[key] += val
    else:
        inventory[key] = val

print(inventory)
