def add(*args):
    result = 0
    for num in args:
        result = result + num
    return result
def sub(*args):
    result = args[0]
    for num in args[1:]:
        result = result - num
    return result
def multiply(*args):
    result = args[0]
    for num in args[1:]:
        result = result * num
    return result
def division(*args):
    result = args[0]
    for num in args[1:]:
        result = result / num
    return result

numbers = input("Enter numbers to calculate: ")
numbers = numbers.split()
numbers = [float (num) for num in numbers]
operator = input("Enter a operator +, -, *, /: ")


if operator == "+":
    result = add(*numbers)
elif operator == "-":
    result = sub(*numbers)
elif operator == "*":
    result = multiply(*numbers)
elif operator == "/":
    result = division(*numbers)
else:
    print("Invalid Operator")

print(result)

