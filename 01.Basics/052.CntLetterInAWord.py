# Ask for a word and a letter, then count how many times that letter appears. Treat uppercase and lowercase as the same.
# Example: word "Banana", letter "a" → 3

def CntLetter(word,letter):
    cnt = 0
    for w in word:
        if w.lower() == letter.lower():
            cnt += 1
    return cnt

word = input("Enter a word:")
letter = input("Enter a letter:")
print(CntLetter(word, letter))