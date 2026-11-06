"""with open("demo.txt", "w") as file:
    file.write("Python is easy")
print("Data Saved")"""

"""with open("demo.txt", "r") as file:
    content = file.read()
print(content)"""

"""f1 = open("file_1.txt", "x")"""

"""f1 = open("file_1.txt", "r")
data = f1.read()
print(data)"""

"""f1 = open("file_1.txt", "w+")
f1.write("Welcome Python Programming")
print(f1.read())""" #If the file already exist it overrides it or create a new file

"""f1 = open("file_1.txt", "r+") # It can modify only in existig file, raed and write
print(f1.read())
f1.write(", Have a good day")
print(f1.read())
print(f1.tell())""" #It will tell where is cursor right now

"""f1 = open("file_1.txt", "r")
data = f1.read()
print("Number of character: ", len(data))
f1.close()"""

#copying from one file to another
"""f1 = open("file_1.txt", "r")
data = f1.read()
f1.close()

f2 = open("file_2.txt", "w")
f2.write(data)
f2.close()"""

"""try:
    file = open("file_3.txt", "r")
    print(file.read())
    file.close()

except:
    print("File Not Found")"""


"""with open("file_1.txt", "r") as file:
    data = file.read()

count = 0 
vowels = []

for i in data.lower():
    if i in "aeiou":
        count += 1
        vowels.append(i)
print("Number of vowels: ", count)
print("Vowels: ", vowels)"""


"""with open("file_1.txt", "r") as file:
    content = file.read()  # For read
    print(content)"""

"""with open("file_1.txt", "w") as file:
    file.write("Hello Python!\n")
    file.write("Learning File Handling")
print("Data written successfully")"""

"""with open("file_1.txt", "r") as file:
    data = file.read()
print(data)"""

"""with open("file_1.txt", "a") as file:
    file.write("\n File Handling is easy")

with open("file_1.txt", "r") as file:
    print(file.read())"""

"""search_word = input("Enter a word to see if it is in the file: ")

with open("file_1.txt", "r") as file:
    data = file.read()

if search_word.lower() in data.lower():
    print("Word Found")
else:
    print("Not Found")"""

"""from pathlib import Path

Path("file_2.txt").unlink()"""
"""file = open("file_2.txt", "x")
file.close"""

"""import shutil   #shutil for file operations 

shutil.copyfile("file_1.txt", "file_2.txt")"""

try:
    with open("file_3.txt", "x") as file:
        file.write("New file created")
except FileExistsError:
    print("File already exists")




