# Given a list and a window size k, find the largest sum among all groups of k consecutive numbers.
# Example: [2, 1, 5, 1, 3], k = 2 → 8

n = int(input("How many numbers you want to enter:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
win_size = int(input("Enter Window size:"))

current_sum = sum(nums[0:win_size])
max_sum = current_sum

for right in range(win_size, len(nums)):
    current_sum += nums[right] - nums[right - win_size]
    max_sum = max(max_sum, current_sum)

print(max_sum)