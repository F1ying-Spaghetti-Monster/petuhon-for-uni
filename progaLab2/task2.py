"""
Task 2 coded by Savchuk Ivan
"""
def task2():
    print('Variant 21. User inputs whole number N > 1, program outputs largest k\n',
            'for which: 1 + 2 + ... + k <= N also outputs this sum\n')
    while True:
        while True:
            print('Please enter a whole number N > 1, or type "q" to quit')
            temp = input()
            if temp == 'q':
                return None
            try:
                N = int(temp)
                if N <= 1:
                    print('N is too small, try again')
                    continue
                break
            except ValueError:
                print("Couldn't convert to int, try again")
        sum = 1
        k = 1
        while sum <= N:
            k+= 1
            sum+= k
        print(f"Largest k is {k-1}, the sum is {sum-k}, which is <= {N}")
        