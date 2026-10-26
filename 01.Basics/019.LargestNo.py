# Find the largest number in a list using a loop. Don’t use max().
# Example: [4, 9, 2, 7] → 9

n = int(input("Enter how many u want:"))
nums = list(map(int,input("Enter numbers:").split()))[:n]
maxi = nums[0]

for num in nums:
    if num > maxi:
        maxi = num
print(maxi)