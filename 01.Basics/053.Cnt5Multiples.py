# Ask for a list of integers and count how many are divisible by 5.
# Example: [10, 3, 25, 7, 5] → 3

def MuiltipleCnt(nums):
    cnt = 0
    for num in nums:
        if num % 5 == 0:
            cnt += 1
    return cnt

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]

print(MuiltipleCnt(nums))