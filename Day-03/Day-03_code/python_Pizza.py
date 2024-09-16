print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
small_pizza = 15
Medium_pizza = 20
large_pizza = 25
bill = 0

size = size.capitalize()
pepperoni = pepperoni.capitalize()
extra_cheese = extra_cheese.capitalize()

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1

    print(f'Your final bill is: ${bill}.')

elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f'Your final bill is : ${bill}.')
    
else:
    bill = 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f'Your final bill is: ${bill}.')