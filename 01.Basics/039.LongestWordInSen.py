# Ask for a sentence and print its longest word. If there’s a tie, printing either longest word is fine.
# Example: "Python makes coding fun" → coding

sen = input("Enter sentence:")
sen_list = sen.split(" ")
word_len = 0
longest_word = ""

for word in sen_list:
    if len(word) > word_len:
        word_len = len(word)
        longest_word = word
print(longest_word)
