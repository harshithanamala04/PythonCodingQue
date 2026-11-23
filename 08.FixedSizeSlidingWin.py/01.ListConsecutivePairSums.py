# Given a list, print the sum of each pair of neighboring numbers.
# Example: [2, 4, 6, 2] → [6, 10, 8]

n = int(input("How many numbers u want to enter:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]

win_size = 2
pair_sum = sum(nums[0:win_size])

total_sum = [pair_sum]

for right in range(win_size,len(nums)):
    pair_sum += nums[right] - nums[right - win_size]
    total_sum.append(pair_sum)

print(total_sum)


