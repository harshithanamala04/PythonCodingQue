# Given a list, find the largest sum made by any three consecutive numbers.
# Example: [2, 1, 5, 1, 3, 2] → 9

n = int(input("How many numbers u want to enter:"))
nums = list(map(int,input("enter Numbers:").split()))[:n]
win_size = 3

current_sum = sum(nums[0:win_size])
best_sum = current_sum

for right in range(win_size, len(nums)):
    current_sum += nums[right] - nums[right - win_size]
    best_sum = max(current_sum, best_sum)

print(best_sum)