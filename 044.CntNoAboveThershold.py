# Ask for a list of numbers and a threshold. Count how many numbers are greater than the threshold.
# Example: [3, 8, 5, 10], threshold 5 → 2

n = int(input("How many numbers u want to enter:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
threshold = int(input("Enter threshold:"))

cnt = 0

for num in nums:
    if num > threshold:
        cnt += 1
print(cnt)