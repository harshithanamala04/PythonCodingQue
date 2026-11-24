# Given a list and a window size k, print the sum of every group of k consecutive numbers.
# Example: [2, 4, 6, 2], k = 3 → [12, 12]

n = int(input("How many numbers u want to enter:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
win_size = int(input("Enter window size:"))

current_sum = sum(nums[0:win_size])
sum_set = [current_sum]

for right in range(win_size, len(nums)):
    current_sum += nums[right] - nums[right - win_size]
    sum_set.append(current_sum)

print(sum_set)