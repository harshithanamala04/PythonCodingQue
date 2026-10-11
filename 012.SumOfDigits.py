# Ask for a positive integer and print the sum of its digits.
# Example: 572 → 14

# while loop takes O(logN)

def digitsSum(n):
    sum = 0
    while n != 0:
        rem = n % 10
        sum += rem
        n //= 10
    return sum

num = int(input("Enter Number:"))
print(digitsSum(num))


