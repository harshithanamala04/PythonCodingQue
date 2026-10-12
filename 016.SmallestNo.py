# Find the Smallest Number
# Given a list of numbers, find the smallest using a loop. Don’t use min().
# Example: [8, 3, 6, 1] → 1

n = int(input("Enter how many number u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]

mini = nums[0]
for num in nums:
    if num < mini:
        mini = num
print(mini)