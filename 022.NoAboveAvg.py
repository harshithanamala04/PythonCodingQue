# Numbers Above the Average
# Find the average of a list, then print how many numbers are greater than that average.
# Example: [2, 4, 6] → average 4, count 1.

n = int(input("Enter how many you want:"))
nums = list(map(int,input("Enter numbers:").split()))[:n]
total = cnt = 0

for num in nums:
    total += num
average = total/n

for num in nums:
    if num > average:
        cnt += 1
print(f"Average {average}, count {cnt}.")
