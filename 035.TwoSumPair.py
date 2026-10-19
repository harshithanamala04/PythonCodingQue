# Given a list and a target, find two different elements that add to the target. Show the pair, or report that none exists.
# Example: [3, 2, 4], target 6 → [2, 4]

n = int(input("how many numbers you want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
target = int(input("Enter target:"))

nums.sort()
left = 0
right = len(nums) - 1

while left < right:
    if nums[left] + nums[right] == target:
        print(nums[left], nums[right])
        break

    elif nums[left] + nums[right] > target:
        right -= 1

    else:
        left += 1

else:
    print("Target is not found..")