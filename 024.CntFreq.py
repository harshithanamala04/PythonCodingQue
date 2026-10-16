# Given a list of numbers, count how many times each number appears.
# Example: [2, 1, 2, 3, 1, 2] → 2 appears 3 times, 1 appears 2 times, 3 appears 1 time

n = int(input("Enter how many no. you want:"))
nums = list(map(int,input("Enter the numbers:").split()))[:n]

cnt_dict = {}

for num in nums:
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1

for key,val in cnt_dict.items():
    print(f"{key} appears {val} time")

# print(cnt_dict)