def is_prime(number):
    if number %2 == 0:
        if number == 2:
            return True
        return False

    for i in range(3, number, 2):
        if number %i == 0:
            return False
    #this loop can be optimized, checking i > sqrt(number) isn't necessary
    #this wasn't done because the task said to implement like this
    if number == 1:
        return False
    return True

def main1():
    print('Завдання 1, створити функцію, що перевіряє чи ціле число n просте\n',
            'алгоритм перевірки - первірка остачі від ділення на 2 та всі непарні числа до n', sep='')
    while True:
        while True:
            try:
                num = int(input('please enter positive integer value: '))
            except ValueError:
                print('this is not an integer, ', end='')
                continue
            if num < 0:
                print('this is negative, ', end='')
                continue
            break
        print(is_prime(num))

        # for i in range(100):    #uncomment this to see check is_prime() for first 100 numbers
        #     print(i, is_prime(i))
        if input('please enter q to exit or anything else to run again: ').lower() == 'q':
            break

if __name__ == '__main__':
    main1()