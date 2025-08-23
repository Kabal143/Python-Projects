print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.00")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.00")
    else:
        bill = 12
        print("Adult tickets are $12.00")
    want_photo = input("Want to take photo take for only $3? Type y for Yes or n for No.")
    if want_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride the rollercoaster :(")