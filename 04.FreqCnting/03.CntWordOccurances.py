# Ask for a sentence and a word, then count how many times that word appears. Treat uppercase and lowercase as the same.
# Example: sentence "Cat dog cat", word "cat" → 2

sen = input("Enter Sentence:").lower()
sen_list = sen.split()

word = input("Enter word to search:").lower()
cnt = 0

for w in sen_list:
    if w  == word:
        cnt += 1
        
print(cnt)
