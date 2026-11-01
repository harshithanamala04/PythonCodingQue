# Check a near-palindrome: Given a word, check whether it becomes a palindrome after removing at most one character. 
# Example: racecar → yes; abca → yes.

# If it's already a perfect palindrome (like "racecar"), the answer is Yes (you removed 0 characters).
# If deleting exactly one character makes it a palindrome (like "abca"), the answer is Yes.
# If it requires removing 2 or more characters to fix it (like "abcde"), the answer is No.

# word = input("Enter a word:")

# left = 0
# right = len(word) - 1
# skip = 0

# while left < right:
#     if word[left] == word[right]:
#         left += 1
#         right -= 1
#     else:
#         left += 1
#         skip += 1
# if skip <= 1 :
#     print("Yes It's a palindrome")
# else:
#     print("Not a palindrome...")
