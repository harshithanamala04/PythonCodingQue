# Ask for a sentence and print its words in reverse order. Keep each word spelled normally.
# Example: "Python makes coding fun" → "fun coding makes Python"

sen = input("Enter Sentence:")
sen_list = sen.split()

reverse_words = []
for word in range(len(sen_list)-1, -1, -1):
    reverse_words.append(sen_list[word])

print(" ".join(reverse_words))