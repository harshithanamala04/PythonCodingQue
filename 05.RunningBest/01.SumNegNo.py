# it scan items once while keeping track of the best value found so far. It applies to finding the longest word.

# Given a list of integers, calculate the sum of only the negative numbers.
# Example: [-3, 5, -2, 0] → -5

n = int(input("How many Numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
NegSum = 0

for num in nums:
    if num < 0:
        NegSum += num
print(NegSum)
