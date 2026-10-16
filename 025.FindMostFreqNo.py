# Given a list, find the number that appears most often. You may assume there’s one clear winner.
# Example: [4, 2, 4, 3, 4, 2] → 4

n = int(input("Enter how many no. you want:"))
nums = list(map(int,input("Enter the numbers:").split()))[:n]

cnt_dict = {}

for num in nums:
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1

max_cnt = 0
winner_key = 0
for key,val in cnt_dict.items():
    if max_cnt < val:
        max_cnt = val
        winner_key = key
print(winner_key)