# Given a sentence, print one of its shortest words.
# Example: "coding is fun" → "is"

sen = input("Enter Sentence:")
sen_list = sen.split()

mini = ""

for word in range(len(sen_list)-1):
    if len(sen_list[word]) > len(sen_list[word + 1]):
        mini = sen_list[word]

print(mini)