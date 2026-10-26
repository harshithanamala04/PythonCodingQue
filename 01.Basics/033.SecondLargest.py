# Find the second-largest distinct number in a list.
# Example: [5, 1, 5, 3] → 3

n = int(input("How many no u want:"))
nums = list(set(list(map(int, input("Enter Nums:").split()))[:n]))
# nums = list(set(map(int,input("Enter nums:").split())))[:n]
# If our input list is [5, 5, 3], when the loop checks the second 5, it will skip the if block (since 5 > 5 is False). Then it hits the elif block, checking if 5 > sec_maxi and 5 != 5. Since 5 != 5 is False, it skips it too.

maxi = sec_maxi = float('-inf')
# We can use -ve infinity to represent the lowest possible starting boundary
for num in nums:
    if num > maxi:
        sec_maxi = maxi
        maxi = num
    elif num > sec_maxi and num != maxi:
        sec_maxi = num

if sec_maxi == float('-inf'):
    print("There is no second largest distinct number in the list")
else:
    print(sec_maxi)
