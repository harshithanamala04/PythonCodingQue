# Count matching pairs: Given a sorted list and a target, count how many pairs of different elements add up to the target. 
# Example: [1, 2, 3, 4, 5], target 6 → 2 pairs.

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
target = int(input("Enter Target Number:"))

cnt = 0
left = 0
right = n - 1

while left < right:
    if nums[left] + nums[right] == target:
        cnt += 1
        left += 1
        right -= 1
    elif nums[left] + nums[right] > target:
        right -= 1
    else:
        left += 1
print(cnt)