# Given a list and a number, count how many neighboring pairs have a sum greater than that number.
# Example: [2, 4, 6, 2], threshold 9 → 1

n = int(input("How many numbers u want to enter:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
th = int(input("Enter Thershold value:"))

win_size = 2
pair_sum = sum(nums[0:win_size])
cnt = 0

# Check the initial window first
if len(nums) >= win_size and pair_sum > th:
    cnt += 1


for right in range(win_size, len(nums)):
    pair_sum += nums[right] - nums[right - win_size]

    if pair_sum > th:
        cnt += 1

print(cnt)