def check_freq(string):
    freq = {}

    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
word = input("Enter a word to see its frequency: ").lower()
print(check_freq(word))