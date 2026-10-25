# Ask for a list of integers and count how many are greater than 10.
# Example: [4, 12, 10, 25] → 2

def GreaterThanTen(nums):
    cnt = 0
    for num in nums:
        if num > 10:
            cnt += 1

    return cnt

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]

print(GreaterThanTen(nums))