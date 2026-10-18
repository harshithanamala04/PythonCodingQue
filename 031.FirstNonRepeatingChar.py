# Given a word, find the first character that appears only once.
# Example: "swiss" → "w"

word = input("Enter word:")

word_cnt = {}

for w in word:
    if w in word_cnt:
        word_cnt[w] += 1
    else:
        word_cnt[w] = 1

winner_char = 0
for k,v in word_cnt.items():
    if v == 1:
        winner_char = k
        print(winner_char)
        break
else:
    print("Every Character is repeating..")
