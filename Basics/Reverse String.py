"""def reverse_string(str):
    reverse = ""
    for i in str:
        reverse = i + reverse
    return reverse
string = input("Enter a string: ")
print(reverse_string(string))"""

string = input("Enter a word: ")
reverse = ""
for i in string:
    reverse = i + reverse
print("Revrsed: ", reverse)