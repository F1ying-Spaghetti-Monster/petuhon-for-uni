from random import *

def replace_zeros(list1):
    list_size = len(list1)
    for idx, i in enumerate(list1):
        if i == 0:
            list1[idx] = list1[idx-1] + list1[(idx+1)% list_size]
    #replacing is done iteratively, so if we have 2+ zeroes in a row
    #the second zero will be affected by changed value of the first
    #if we want to sum the first 0 when calculating the second 0, we can create 
    #a second list, where we do all replacement and keep original values in the first.

def main1():
    print('Завдання 1, у списку з цілими числами:',
            '-Поміняти 1-ий елемент з останнім, другий з передостаннім і т.п.',
            '-Замінити нулі на суму сусідніх елементів, для крайніх брати елементи з іншого кінця\n', sep='\n')
    while True:
        data = input('press q to exit, enter list of integers or press enter to autogenerate\n')
        if data.lower() == 'q':
            return
        
        if data == '':
            list_size = 20
            try:
                list1 = sample(range(0, 100), list_size)   
            except TypeError:
                print('check LIST_SIZE value')
                continue
            for _ in range(3):  #assuring there are a few zeroes
                list1[randint(0, list_size-1)] = 0

        else:
            list1 = []
            for i in data.split():
                try:    #ignoring all non int elements
                    list1.append(int(i))
                except ValueError:
                    continue
            if list1 == []:
                print('no elements in list, try again')
                continue

        print(f'your list is:\n{list1}')

        list1.reverse()
        print(f'list after "swapping":\n{list1}')
        #swaping all elements is equivalent to just reversing
        #to swap by hand you can do: a[i], a[-(i+1)] = a[-(i+1)], a[i]

        replace_zeros(list1)
        print(f'"swapped" list after replacing zeroes:\n{list1}')

if __name__ == '__main__':
    main1()