#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console

word_count = 0

file = open("song_lyrics.txt", "r")
content = file.read().lower()
file.close()

print("Which 5 words are you looking for in this song?")

word1 = input("word1: ").lower()
word2 = input("word2: ").lower()
word3 = input("word3: ").lower()
word4= input("word4: ").lower()
word5 = input("word5: ").lower()

print("The word you choose are", word1,word2,word3,word4,word5)

word_dict = {}
word_dict[word1] = content.count(word1)
word_dict[word2] = content.count(word2)
word_dict[word3] = content.count(word3)
word_dict[word4] = content.count(word4)
word_dict[word5] = content.count(word5)


print("\nWord Frequencies:")
print(word_dict)

