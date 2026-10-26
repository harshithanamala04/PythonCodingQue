# Ask for a list of integers and count how many are negative.
# Example: [4, -2, 0, -7, 3] → 2

def Neg(nums):
    cnt = 0
    for num in nums:
        if num < 0:
            cnt += 1
    return cnt

n = int(input("Enter how many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
print(Neg(nums))