# Given a sorted list, remove repeated neighboring values so each value appears once. Keep the result sorted.
# Example: [1, 1, 2, 2, 2, 4] → [1, 2, 4]

n = int(input("How many Numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]

marker = 0
for explorer in range(1,n):
    if nums[marker] != nums[explorer]:
        marker += 1
        nums[marker] = nums[explorer]

print(nums[:marker + 1])