# Given a list of numbers, calculate the average, then count how many numbers are greater than it.
# Example: [2, 4, 6, 8] → average 5, count 2

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
nums_sum = 0

for num in nums:
    nums_sum += num

avg = nums_sum / n

cnt = 0
for num in nums:
    if num > avg:
        cnt += 1
print(f"average is {avg} and the count above the average is {cnt}")
