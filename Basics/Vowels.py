def vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    output = ""

    for i in word:
        if i in vowels:
            count += 1
            output +=i
    return output, count
word2 = input("Enter a word: ")
count, output = vowels(word2)
print("Vowels: ", output)
print("Count: ",count)



