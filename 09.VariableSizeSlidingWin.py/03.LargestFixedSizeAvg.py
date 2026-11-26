# Given a list and a window size k, find the largest average among all consecutive groups of k numbers.
# Example: [1, 3, 2, 6, 1], k = 2 → 4

n = int(input("How many numbers u want to enter:"))
nums = list(map(int, input("Enter Numbers:").split()))[:n]
win_size = int(input("Enter window size:"))

curr_sum = sum(nums[0:win_size])
max_sum = curr_sum  

for right in range(win_size, len(nums)):
    curr_sum += nums[right] - nums[right - win_size]
    max_sum = max(max_sum, curr_sum)

print(max_sum / win_size)


# n = int(input("How many numbers u want to enter:"))
# nums = list(map(int,input("Enter Numbers:").split()))[:n]
# win_size = int(input("Enter window size:"))

# curr_sum = sum(nums[0:win_size])
# avg_sum = [curr_sum]

# for right in range(win_size, len(nums)):
#     curr_sum += nums[right] - nums[right - win_size]
#     avg_sum.append(curr_sum/win_size)

# print(max(avg_sum))