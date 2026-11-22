# Given a sentence, print one of its shortest words.
# Example: "coding is fun" → "is"

sen = input("Enter sentence:")
words = sen.split()

print(min(words, key = len))