# Given a sentence, count how many words have more than four letters.
# Example: "I enjoy learning Python" → 3

sen = input("Enter sentence:")
sen_list = sen.split(" ")
# Using split() without an argument would also handle extra spaces between words.
cnt = 0

for word in sen_list:
    if len(word) > 4:
        cnt += 1

print(cnt)