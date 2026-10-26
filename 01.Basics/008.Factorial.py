# Ask for a non-negative integer n and calculate n! using a loop.
# Example: 5! = 5 × 4 × 3 × 2 × 1 = 120. Remember that 0! is 1.

n = int(input("enter number:"))
prod = 1
for i in range(n,1,-1):
    prod *= i
print(prod)

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n - 1)

# num = int(input("Enter number:"))
# print(fact(num))

# Point to remember when using recursion use base case then followed by recursive case..
