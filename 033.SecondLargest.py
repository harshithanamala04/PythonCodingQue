# Find the second-largest distinct number in a list.
# Example: [5, 1, 5, 3] → 3

n = int(input("How many no u want:"))
nums = list(map(int,input("Enter nums:").split()))[:n]

maxi = nums[0]
sec_maxi = 0
for num in nums:
    if num > maxi:
        sec_maxi = maxi
        maxi = num
    elif num > sec_maxi and num != maxi:
        sec_maxi = num

print(sec_maxi)