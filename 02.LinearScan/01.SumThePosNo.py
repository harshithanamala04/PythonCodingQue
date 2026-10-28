# A linear scan checks items one by one from beginning to end.
# It’s useful for tasks like counting matches, finding the smallest value, or checking whether something is present. 
# For n items, it takes O(n) time. If you only keep a running count or current best value, it uses O(1) extra space.

# For eg [3, 8, 7, 2]

# A linear scan checks each number in order: 3 → 8 → 7. 
# Once it finds 7, it can stop. 
# If the number isn’t in the list, it must check every item.
# For a list of n items, that’s O(n) time. If we only keep track of what we’re currently checking, it uses O(1) extra space.

# Sum the Positive Numbers
# Ask for a list of integers and calculate the sum of only the positive numbers.
# Example: [4, -2, 0, 7, -1] → 11

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
total = 0

for num in nums:
    if num > 0:
        total += num

print(total)
