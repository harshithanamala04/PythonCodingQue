# Create a new list containing each value only once, in the order it first appeared.
# Example: [3, 1, 3, 2, 1] → [3, 1, 2]

n = int(input("Enter how many u want: "))
nums = list(map(int, input("Enter numbers: ").split()))[:n]

seen = set()
unique_nums = []

for num in nums:
    if num not in seen:
        seen.add(num)
        unique_nums.append(num)

print(unique_nums)



