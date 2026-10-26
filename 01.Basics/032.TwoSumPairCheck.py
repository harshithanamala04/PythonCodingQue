# Given a list of numbers and a target, determine whether two different list elements add up to the target. Don’t use the same element twice.
# Example: [2, 7, 11, 15], target 9 → Yes; target 10 → No

n = int(input("how many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
target = int(input("Enter target:"))

nums.sort()

left = 0
right = len(nums) - 1

while left < right:
    if nums[left] + nums[right] == target:
        print("Target is found")
        break

    elif nums[left] + nums[right] > target:
        right -= 1

    else:
        left += 1

else:
    print("Not found")
