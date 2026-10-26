# Given a list of integers, count how many are positive, negative, and zero.
# Example: [4, -2, 0, 7, -1] → 2 positive, 2 negative, 1 zero.

n = int(input("Enter how many u want:"))
nums = list(map(int,input("enter numbers:").split()))[:n]
zero_cnt = pos_cnt = neg_cnt = 0

for num in nums:
    if num == 0:
        zero_cnt += 1
    elif num > 0:
        pos_cnt += 1
    else:
        neg_cnt += 1 
print(f"{pos_cnt} Positive, {neg_cnt} Negative, {zero_cnt} zero")