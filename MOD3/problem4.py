#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word = input("Please write a word ")
index1 = int(input("Please write the first index"))
index2 = int(input("Please write the second index"))
sliced_word = word[index1:index2]
print(sliced_word)
