# Ask for a sentence and create a list of words that start with a, e, i, o, or u. Treat uppercase and lowercase letters the same.
# Example: "An apple and a pear" → ["An", "apple", "and"]

def startVowel(sen_list):
    worsdWithVowels = []
    vowels = 'aeiouAEIOU'
    for word in sen_list:
        if word[0] in vowels:
            worsdWithVowels.append(word)
    return worsdWithVowels

sen = input("Enter Sentence:")
sen_list = sen.split()

print(startVowel(sen_list))