# Check for a Number
# Ask for a list of integers and another number. Print whether that number appears in the list.
# Example: list [3, 8, 2, 5], number 2 → Found

n = int(input("How many Numbers u want:"))
nums = list(map(int,input("Enter Numbers:").split()))[:n]
target = int(input("Enter the number to search:"))

for num in nums:
    if num == target:
        print(f"Number {num} is found")
        break
    
else:
    print("Number not in the list..")