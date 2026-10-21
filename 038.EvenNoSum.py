# Given a list of integers, find the sum of the even numbers.
# Example: [2, 5, 8, 1] → 10

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
total = 0

for num in nums:
    if num % 2 == 0:
        total += num
print(total)