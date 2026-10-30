# Both pointers move from left to right. 
# One scans the items; the other marks where the next kept item belongs. 
# This differs from the two pointers that start at opposite ends and move toward each other.

# Given a list and a target, remove every occurrence of the target while keeping the other numbers in their original order.
# Example: [2, 1, 2, 3, 2], target 2 → [1, 3]

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
target = int(input("Enter Target Number:"))

marker = 0
for explorer in range(0,n):
    if nums[explorer] != target:
        nums[marker] = nums[explorer]
        marker += 1

print(nums[:marker])