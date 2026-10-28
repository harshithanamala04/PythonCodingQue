# A frequency map uses a dictionary to record how often each item appears.
# For example, in [2, 1, 2], the counts are 2: 2 and 1: 1. 
# This is useful when a problem asks about repeats or counts.
# Processing n items takes O(n) time and typically uses O(k) space for k distinct items.

# Ask for a list of integers and find the sum of numbers divisible by 3.
# Example: [3, 5, 12, 7] → 15

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
total = 0

for num in nums:
    if num % 3 == 0:
        total += num
print(total)