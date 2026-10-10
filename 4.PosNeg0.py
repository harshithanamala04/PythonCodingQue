# Ask for a number and print Positive, Negative, or Zero.
# Example: input -4 → output Negative

num = int(input("Enter Number:"))
if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negative")