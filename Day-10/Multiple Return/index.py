def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


# print(is_leap_year(year=2400))
# print(is_leap_year(year=2000))
# print(is_leap_year(year=2100))
# print(is_leap_year(year=1989))
# print(2100 % 400)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print(add(2, multiply(5, divide(8, 4))))


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))
