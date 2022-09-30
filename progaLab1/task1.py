"""
Task 1 variant 21
coded by Savchuk Ivan
with given number 'a' and only using
multiplication, calculate:
1) a^4 with 2 operations
2) a^6 with 3 operations
3) a^15 with 5 operations
"""


def printPower4(a):
    a *= a  # a^2
    a *= a  # a^4
    print("a^4 is", a)


def printPower6(a):
    a *= a*a  # a^3
    a *= a  # a^6
    print("a^6 is", a)


def printPower15(a):
    temp = a  # store original value for future use
    a *= a  # a^2
    a *= a  # a^4
    a *= temp  # a^5
    a *= a*a  # a^15
    print("a^15 is", a)


"""
hopefully usinng *= isn't "against the rules"
as it was done for better readability and
it doesn't affect the amount of operations.
Code above can be just as well written with:
a = a*a
"""

while True:
    temp = input("type a number you want to test, or type \"quit\" \n")
    if temp == "quit":
        break
    try:  # check if can converted to int
        a = int(temp)
    except ValueError:
        try:  # check if can converted to float
            a = float(temp)
        except ValueError:
            try:  # check if can conver to complex
                a = complex(temp)
            except Exception:
                print("couldn't convert, please try again,", end=" ")
                continue
    try:
        printPower4(a)
        printPower6(a)
        printPower15(a)
    except MemoryError:  # might not have enough memory to allocate big number
        print("number too big,", end=" ")
