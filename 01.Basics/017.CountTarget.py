# Count a Target Number
# Ask for a list of numbers and a target number, then count how many times the target appears.
# Example: list [2, 5, 2, 7, 2], target 2 → 3

n = int(input("Enter how many u want:"))
nums = list(map(int,input("Enter number:").split()))[:n]
target = int(input("Enter target:"))
cnt = 0
nums.sort()

for num in nums:
    if num == target:
        cnt += 1
    elif num > target:
        break # no need to look at the rest of ele
          
print(cnt)