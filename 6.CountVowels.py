# Ask for a word and count how many vowels it contains (a, e, i, o, u). Treat uppercase and lowercase letters the same.
# Example: input Python → output 1

def cnt_vowels(word):
    vowels = ['a','e','i','o','u']
    cnt = 0

    for i in word:
        if i in vowels:
            cnt += 1
    return cnt

w = input("enter word:").lower()
print(cnt_vowels(w))