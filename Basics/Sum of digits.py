num = 1234
total = 0

while num > 0:
    digits = num % 10
    total += digits
    num = num // 10
print("Sum of digits: ", total)