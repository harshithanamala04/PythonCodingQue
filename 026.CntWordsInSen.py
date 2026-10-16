# Ask for a sentence and count how many times each word appears. Treat uppercase and lowercase versions of a word as the same.
# Example: Cat dog cat → cat: 2, dog: 1

sen = input("Enter Sentence:").lower()
sen_list = sen.split(' ')

word_dict = {}

for word in sen_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
print(word_dict)