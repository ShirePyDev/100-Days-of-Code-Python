from art import logo
print(logo)



def add(n1, n2):
    return n1 + n2
def subt(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subt,
    "*": mult,
    "/": divide
}
def keep(n1, operations, n2):
    if operations == "/":
        if n2 == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return n1 / n2
    elif operations == "*":
        return n1 * n2
    elif operations == "+":
        return n1 + n2
    elif operations == "-":
        return n1 - n2
    else:
        print("Invalid number")
        return  None

should_continue = True
result = 0
while True:
        user_number = float(input("What is your number: "))
        user_operation = input("+\n-\n*\n/\n Pick an operation: ")
        user_second_number = float(input("What is your second number: "))
        result = keep(n1=user_number, operations= user_operation, n2=user_second_number)
        print(f"{user_number} {user_operation} {user_second_number} = {result}")
        previous = input("Type 'y' if you want to continue previous result or 'n' to stop the game: ")
        if previous == "y":
            user_operation = input("+\n-\n*\n/\n Pick an operation: ")
            user_second_number = float(input("What is your second number: "))
            result = keep(n1=user_number, operations= user_operation, n2=user_second_number)
            print(f"{user_number} {user_operation} {user_second_number} = {result}")
        else:
            break


