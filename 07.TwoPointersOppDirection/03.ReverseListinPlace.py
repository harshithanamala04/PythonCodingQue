# Reverse a list by swapping items, without creating a second list.
# Example: [2, 5, 7, 9] → [9, 7, 5, 2]

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]

left = 0
right = n - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1

print(nums)