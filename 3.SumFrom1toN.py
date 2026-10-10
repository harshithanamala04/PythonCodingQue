#  Ask for a positive integer N, then calculate and print the sum of all integers from 1 through N.
#  Example: input 5 → output 15 because 1 + 2 + 3 + 4 + 5 = 15

num = int(input("Enter number:"))

sum = 0

for i in range(1,num + 1):
    sum += i
print(sum)