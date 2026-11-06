def add(*args):
    result = 0
    for i in args:
        result = result + i
    return result

numbers = input("Enter numbers to perform addition: ")
numbers = numbers.split()
numbers = [float(i) for i in numbers]
result = add(*numbers)
print("Result is", result)