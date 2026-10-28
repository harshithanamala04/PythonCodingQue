# Ask for a sentence and count the words that start with the letter s, ignoring uppercase or lowercase.
# Example: "Sam sees seven stars" → 4

sen = input("Enter Sentence:").lower()
sen_list = sen.split()
cnt = 0

for word in sen_list:
    if word[0] == 's':
        cnt += 1

print(cnt)
