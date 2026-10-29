# Given a sentence, print its longest word. If there’s a tie, either longest word is fine.
# Example: "I enjoy learning Python" → "learning"

sen = input("Enter Sentence:")
sen_list = sen.split()
longest_word = ""
longest_word_len = 0


for word in sen_list:
    if len(word) > longest_word_len:
        longest_word = word
        longest_word_len = len(word)

print(longest_word)