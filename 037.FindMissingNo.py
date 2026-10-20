# Find the Missing Number
# A list contains distinct numbers from 1 through n, with one number missing. Find it.
# Example: [1, 2, 4, 5] → 3

nums = list(map(int,input("Enter Numbers:").split()))
missing = 0

for i in range(1,len(nums)):
    if i not in nums:
        missing = i
        print(missing)
        break

