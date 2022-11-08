"""
Task 1 coded by Savchuk Ivan
"""
def task1():
    print('variant #21 ∑(2*x^i  -1)/n-1  | i from 1 to n')

    while True:
        while True:
            print('Please enter a real value of x or print "q" to quit:')
            temp = input()
            if temp == 'q':
                return None
            try:
                x = float(temp)
                break
            except ValueError:
                print("Sorry, couldn't convert to float, try again")
                continue

        while True:
            print('Please enter a whole number n:')
            temp = input()
            if temp == 'q':
                return None
            try:
                n = int(temp)
                if n < 1:  # this check is optional, without it program returns sum = 0.0
                    print('Sorry, ivalid input, n must be > 1')
                    continue
                break
            except ValueError:
                print("Sorry, couldn't convert to integer, try again")
                continue
            
        temp = 0.0
        noErrors = True
        for i in range(n):
                try:
                    temp += ((x ** (i+1)) * 2 - 1) / (n - 1)
                except ZeroDivisionError:
                    noErrors = False
                    print('Invalid formula, division by zero')
                except ValueError:
                    noErrors = False
                    print('Invalid formula')
                    break
        if noErrors:
            print('sum =', round(temp, 2))
