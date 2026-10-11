# Ask for a word and print it backwards using a loop. For example, cat → tac. Try not to use slicing ([::-1]) yet.

word = input("Enter a word:")

for i in range(len(word)-1,-1,-1):
    print(word[i],end="")
