# Find the length of the longest consecutive section whose sum is at most the limit.
# Example: [2, 1, 3, 2, 1], limit 5 → 2

n = int(input("How many numbers u want to enter:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
limit = int(input("Enter the limit val:"))

left = 0
win_sum = 0
max_len = 0

for right in range(len(nums)):
    win_sum += nums[right]

    while win_sum > limit:
        win_sum -= nums[left]
        left += 1

    curr_len = right - left + 1
    max_len = max(curr_len, max_len)

print(max_len)