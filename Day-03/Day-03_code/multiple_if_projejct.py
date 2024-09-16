print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child Tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth Tickets are $7.")

    elif age >= 45 and age <= 55:
        # bill = 0
        print("Age of 45 and 55 Modifier $0.")

    else:
        bill = 12
        print("Adult Tickets are $12.")

    cart = input("DO you want a photo? Type Y for yes or N for no: ")
    cart = cart.capitalize()
    if cart == "Y":
        bill += 3
    print(f'Your total bill is {bill} ')
else:
    print("Sorry you have to grow taller before you can ride.")