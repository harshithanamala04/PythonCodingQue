# Given a sorted list and a target, determine whether two different numbers add up to the target.
# Example: [1, 3, 4, 6, 8], target 10 → Yes

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
target = int(input("Enter Target Number:"))

left = 0
right = n - 1

while left < right:
    if nums[left] + nums[right] == target:
        print("Yes target Found")
        break
    elif nums[left] + nums[right] > target:
        right -= 1
    else:
        left += 1

else:
    print("Target Not Found")