# Ask for a positive integer and determine whether it reads the same forwards and backwards.
# Example: 121 → palindrome; 123 → not a palindrome.

def palindrome(num):
    initial_num = num 
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    return rev == initial_num

n = int(input("Enter number:"))
print(palindrome(n))