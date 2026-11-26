# Find the length of the shortest consecutive section whose sum is at least the target. If no section reaches it, print 0.
# Example: [2, 1, 3, 2, 1], target 5 → 2

n = int(input("How many numbers u want to enter:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
limit = int(input("Enter the limit val:"))

left = 0
win_sum = 0
# min_len = 0
min_len = float('inf') 

for right in range(len(nums)):
    win_sum += nums[right]

    # Shrink while the window is STILL valid (>= limit)
    while win_sum >= limit:
        curr_len = right - left + 1
        min_len = min(curr_len, min_len)
        win_sum -= nums[left]
        left += 1

if min_len == float('inf'):
    print(0)
else:
    print(min_len)