string = input("Enter a string: ")
string = string.lower()
if string == string[::-1]:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
