# Move every 0 in a list to the end while keeping the other numbers in their original order.
# Example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]

n = int(input("How many u want to enter:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]

marker = 0
for explorer in range(1,len(nums)):
    if nums[marker] != nums[explorer]:
        nums[marker], nums[explorer] = nums[explorer], nums[marker]
        marker += 1
print(nums)
