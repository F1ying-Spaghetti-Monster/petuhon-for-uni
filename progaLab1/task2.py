"""
Task 2 variant 21
coded by Savchuk Ivan
Enter 4 numbers a, b, c, d
Check if any of them = d
if neither = d, find max(d-a, d-b, d-c)
if a, b or c = d, output it on the screen
"""

while True:
    values = input(
        "please enter 4 real numbers separated by spaces or \"quit\" \n").split(' ')
    if values[0] == "quit":
        break
    if len(values) != 4:
        print("invalid input ", end="")
        continue
    try:  # check if int
        a, b, c, d = [int(values[i]) for i in range(4)]
    except ValueError:
        try:  # check if float
            a, b, c, d = [float(values[i]) for i in range(4)]
        except Exception:
            # no check for complex, because max() only works with real numbers
            print("invalid input ", end="")

    """
    The program doesn't allow for a, b, c, d to have different data types
    this is intended behaviour, to ensure there are no errors in the future
    to allow different types you can assign a, b, c, d separately
    this would need running datatype checks for each assigning
    and properly handling invalid 2nd 3rd and 4th input using more loops (so you don't delete previous values)
    """

    output = ""  # output will store what values if any share value
    if a == d:
        output += 'a'
    if b == d:
        output += 'b'
    if c == d:
        output += 'c'
    if output:  # string can be used as a boolean, False if empty, True if not empty
        # if output isn't empty, there must be at least 1 number = d, which is stored in output
        print("d shares value with", end=" ")
        print(", ".join(output[i] for i in range(len(output))))
    else:
        print("no match, max =", max(d-a, d-b, d-c))
