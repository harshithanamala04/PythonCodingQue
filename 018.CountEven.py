# Given a list of integers, count how many are even.
# Example: [2, 5, 8, 7, 10] → 3

n = int(input("Enter how many no you want:"))
nums = list(map(int,input("Enter numbers:").split()))[:n]
cnt = 0

for num in nums:
    if num % 2 == 0:
        cnt += 1

print(cnt)
