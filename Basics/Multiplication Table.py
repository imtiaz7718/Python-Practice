num = int(input("Enter a number to see its Multiplication Table: "))
r = int(input("Enter range: "))

for i in range(r+1):
    print(f"{num} x {i} = {num * i}") 