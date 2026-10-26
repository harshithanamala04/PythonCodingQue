# Ask for a list of integers and count how many are greater than zero.
# Example: [3, -1, 0, 7, -4] → 2

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]

cnt = 0

for num in nums:
    if num > 0:
        cnt += 1
print(cnt)