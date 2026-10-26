# Decide whether two words contain the same letters, ignoring uppercase and lowercase.
# Example: listen, silent → anagrams; hello, world → not anagrams.

word1 = input("Enter 1st word:").lower()
word2 = input("Enter 2nd word:").lower()

if len(word1) == len(word2):
    word1_dict = {}
    word2_dict = {}

    for word in word1:
        if word in word1_dict:
            word1_dict[word] += 1
        else:
            word1_dict[word] = 1

    for word in word2:
            if word in word2_dict:
                word2_dict[word] += 1
            else:
                word2_dict[word] = 1

    if word1_dict == word2_dict:
        print("Words are anagrams")

    else:
        print("Words are not anagrams")