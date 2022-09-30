"""
Task 3 variant 21
coded by Savchuk Ivan
calculate f(x)
f(x) = -x^2 -1.1x + 9 when x <= -3
f(x) = ln(x+3) / (x^2 + 9) when x > -3
"""
from math import log

while True:
    userInput = (input("please type a real number or type \"quit\" \n"))
    if userInput == "quit":
        break
    try:
        x = float(userInput)  # check if input is a real number
    except ValueError:
        print("couldn't convert, ", end="")
        continue
    try:
        if x > -3:
            print("f(x)=", log(x+3)/(x*x+9))
        else:
            print("f(x)=", -x*x-1.1*x+9)
    except MemoryError:
        print("not enough memory ", end="")
    except ValueError:
        print("bad value, function doesn't exist here, ", end="")
    except ZeroDivisionError:
        print("can't divide by zero, ", end="")

        #the quadratic equation in else block can be solved and
        #simplified to (x-x1)(x-x2) format, which would be faster to
        #compute, as it has faster operations
