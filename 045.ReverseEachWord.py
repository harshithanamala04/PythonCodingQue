# Ask for a sentence and print each word reversed, keeping the words in their original order.
# Example: "code every day" → "edoc yreve yad"

sen = input("Enter sentence:")
sen_list = sen.split()
reverse_word = []

for word in sen_list:
    reverse_word.append(word[::-1])
print(" ".join(reverse_word))

