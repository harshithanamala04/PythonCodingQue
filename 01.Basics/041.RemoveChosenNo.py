# Given a list and a number, create a new list without that number. Keep the other numbers in their original order.
# Example: [2, 1, 2, 3, 2], remove 2 → [1, 3]

n = int(input("How many numbers u want:"))
nums = list(map(int,input("Enter Nums:").split()))[:n]
remove_num = int(input("Enter the no. you want to remove from the list:"))

new_list = []

for num in nums:
    if num != remove_num:
        new_list.append(num)
print(new_list)
