# Given a word, determine whether it reads the same forward and backward.
# Example: "level" → Yes; "python" → No

word = input("Enter word:").lower()
left = 0
right = len(word) - 1
is_palindrome = True

while left < right:
    if word[left] == word[right]:
        left += 1
        right -= 1
    else:
        print("Not a palindrome")
        is_palindrome = False
        break

if is_palindrome:
    print("It's a Palindrome")


