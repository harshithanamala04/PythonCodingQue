# Ask for five numbers, store them in a list, and print their total.
# Example: [2, 4, 1] → 7

n = int(input("Enter how many u want to sum:"))
nums = list(map(int,input("Enter numbers:").split()))[:n]
total = 0
for num in nums:
    total += num
print(total)