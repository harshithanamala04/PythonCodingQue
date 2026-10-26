# Ask for a positive integer n. For each number from 1 to n,
# print Fizz if it’s divisible by 3, Buzz if divisible by 5, and FizzBuzz if divisible by both. Otherwise, print the number.
# Example: for 5, print 1, 2, Fizz, 4, Buzz.

def FizzBuzz(num):
    ans = []
    for i in range(1,num+1):
        if i % 3 == 0 and i % 5 == 0:
            ans.append("FizzBuzz")
        elif i % 3 == 0:
            ans.append("Fizz")
        elif i % 5 == 0:
            ans.append("Buzz")
        else:
            ans.append(i)
    return ans

n = int(input("Enter number:"))
print(FizzBuzz(n))
