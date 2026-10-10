# Ask for a number and print its multiplication table from 1 to 10.
# Example: input 3 → print 3 x 1 = 3 through 3 x 10 = 30

n = int(input("Enter Number:"))

for i in range(1,11):
    print(f"{n} * {i} = {n * i}")