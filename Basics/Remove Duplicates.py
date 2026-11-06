"""numbers = [1,4,5,5,5,6,6,3,3,7]
uniuqe = []
for i in numbers:
    if i not in uniuqe:
        uniuqe.append(i)
print("Without duplicates: ", uniuqe)"""

def remove_duplicate(numbers):
    unique = []
    for i in numbers:
        if i not in unique:
            unique.append(i)
    return unique #return should be outside the for and if condition, it should be inside the function

numbers = [1,4,5,5,5,6,6,3,3,7]
result = remove_duplicate(numbers)
print(result)
        