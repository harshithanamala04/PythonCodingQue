# Determine whether the numbers are in non-decreasing order.
# Example: [1, 2, 2, 5] → sorted; [1, 3, 2] → not sorted.

n = int(input("Enter how many you want:"))
nums = list(map(int,input("Enter numbers:").split()))[:n]

# nums_sort = sorted(nums)

# if nums == nums_sort:
#     print("Sorted")
# else:
#     print("Not Sorted")

for i in range(len(nums)-1):
    if nums[i] > nums[i + 1]:
        print("Not sorted")
        break
else:
    print("Sorted")
