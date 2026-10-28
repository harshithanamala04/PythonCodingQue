# A running total keeps a value that you update as you process each item. 
# It’s useful for sums and counts. 
# You start with an initial value, visit the items once, and update the total when needed.
# For n items, this takes O(n) time and O(1) extra space.


# Ask for a list of integers and calculate the sum of only the odd numbers.
# Example: [2, 5, 8, 3] → 8

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
odd_total = 0

for num in nums:
    if num % 2 != 0:
        odd_total += num
print(odd_total)