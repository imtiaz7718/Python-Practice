numbers = [1,2,3,3,3,4,4,5,6]
duplicates = []
for i in numbers:
    if numbers.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
print("Duplicates: ", duplicates)

numbers = [1,2,3,3,3,4,4,5,6]
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print("Unique elements: ", unique)


