# Ask for three numbers and print the largest. Try solving it with if and elif rather than Python’s max().
first = int(input("Enter 1st number:"))
second = int(input("Enter 2nd number:"))
third = int(input("Enter 3rd number:"))

if first <= third and second <= third:
    print(f"Highest number is:{third}")
elif first >= second and first >= third:
    print(f"Highest number is:{first}")
else:
    print(f"Highest number is:{second}")

