# Given a list of numbers, find the first number that appears for a second time. If none repeat, report that.
# Example: [4, 2, 7, 2, 4] → 2

n = int(input("Enter how many no u want:"))
nums = list(map(int,input("Enter numbers:").split()))[:n]

nums_cnt = {}

for num in nums:
    if num in nums_cnt:
        print(num)
        break
    else:
        nums_cnt[num] = 1
else:
    print("No repeating Numbers.")
