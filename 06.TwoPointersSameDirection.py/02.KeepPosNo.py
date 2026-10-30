# Given a list, keep only the positive numbers in their original order.
# Example: [0, 4, -2, 7, -1] → [0, 4, 7]

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]

marker = 0
for explorer in range(0,n):
    if nums[explorer] >= 0:
        nums[marker] = nums[explorer]
        marker += 1

print(nums[:marker])