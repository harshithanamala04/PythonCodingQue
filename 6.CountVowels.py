# Ask for a word and count how many vowels it contains (a, e, i, o, u). Treat uppercase and lowercase letters the same.
# Example: input Python → output 1

word = input("Enter word:").lower()
vowels = ['a','e','i','o','u']
cnt = 0

for i in word:
    if i in vowels:
        cnt += 1
print(cnt)