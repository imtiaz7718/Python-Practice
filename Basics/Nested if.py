pizza = input("Which size of Pizza Do you need(S/M/L): ")
bill = 0
if pizza == "S" or pizza == "s":
    bill += 100
    print(f"Your Pizza is {bill} Rs.")
elif pizza == "M" or pizza == "m":
    bill += 200
    print(f"Your Pizza is {bill} Rs.")
elif pizza == "L" or pizza == "l":
    bill += 300
    print(f"Your Pizza is {bill} Rs.")
else:
    print("Invalid choice")

dips = input("Do you need Dips(Y/N): ")
if dips == "Y" or "y":
    if pizza == "S" or pizza == "s":
        bill += 30
    else:
        bill += 50

cheese = input("Do you need extra cheese(Y/N): ")
if cheese == "Y" or cheese == "y":
    bill += 50

print(f"Your final amount is {bill}") 

