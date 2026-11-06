"""num = int(input("Enter a Number: "))
reverse = 0

while num > 0:
    digit = num % 10                      # gives last number
    reverse = reverse * 10 + digit           
    num = num // 10                    # removes last number
print("Reversed: ", reverse)"""

# 1234

"""digit : 1234 % 10 - 4
reverse : 0 * 10 + 4 - 4
num : 1234 - 123

digit : 123 % 10 - 3
reverse : 4 * 10 + 3 - 43
num : 123 - 12

digit : 12 % 10 - 2
reverse : 43 * 10 + 2 - 432
num : 12 - 1

digit : 1 % 10 - 0.1
reverse : 432 * 10 + 0.1 - 4320.1
num : 1 - 0"""





