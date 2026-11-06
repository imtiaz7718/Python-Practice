word1 = input("Enter a word: ")
word2 = input("Enter a word: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("Anagrams")
else:
    print("Not Anagrams")