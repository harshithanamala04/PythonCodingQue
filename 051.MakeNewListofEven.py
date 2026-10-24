# Ask for a list of integers and create a new list containing only the even numbers, keeping their original order.
# Example: [5, 2, 8, 3, 6] → [2, 8, 6]

def EvenNo(nums):
    evenNo = []
    for num in nums:
        if num % 2 == 0:
            evenNo.append(num)
    return evenNo


n = int(input("How many Numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]

print(EvenNo(nums))