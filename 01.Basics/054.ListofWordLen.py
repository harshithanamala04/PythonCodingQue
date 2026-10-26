# Ask for a sentence and create a list containing the length of each word, in order.
# Example: "Python is fun" → [6, 2, 3]

def SenLen(sen_list):
    word_len = []
    for word in sen_list:
        word_len.append(len(word))
    return word_len

sen = input("Enter Sentence:")
sen_list = sen.split()

print(SenLen(sen_list))
