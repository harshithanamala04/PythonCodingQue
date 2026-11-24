# Given a list, a window size k, and a threshold, count how many consecutive groups of k numbers have a sum greater than the threshold.
# Example: [1, 3, 2, 5, 1], k = 2, threshold 6 → 1

n = int(input("How many numbers u want to enter:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
win_size = int(input("Enter window size:"))
th = int(input("Enter the thershold value:"))

cnt = 0
total = sum(nums[0:win_size])

if total > th:
    cnt += 1

for right in range(win_size, len(nums)):
    total += nums[right] - nums[right - win_size]
    if total > th:
        cnt += 1

print(cnt)