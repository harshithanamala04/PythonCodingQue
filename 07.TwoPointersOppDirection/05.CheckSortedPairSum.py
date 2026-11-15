# Given a sorted list and a target, print whether two different elements add up to the target.
# Example: [1, 2, 4, 7], target 9 → True

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
target = int(input("Enter Target:"))

left = 0
right = len(nums) - 1

while left < right:
    if nums[left] + nums[right] == target:
        print(True)
        break
    elif nums[left] + nums[right] < target:
        left += 1
    else:
        right -= 1

else:
    print(False)