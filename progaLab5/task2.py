def Compress(s, t):
    new_str = ''
    for i in s:
        if i != t:  #if character != t we just add it to new string
            new_str += i
        elif new_str == '': #so we don't try new_str[-1] on empty string
            new_str += i
        elif new_str[-1] == t:  #compare to the previous character, if both = t, don't add
            continue
        else:   #if previous character is different, add
            new_str += i
    return new_str

def main2():
    print('Завдання 2, створити функцію "Compress", яка приймає як аргументи стоку s та символ t\n',
            'Функція має повертати цю строку, замінивши множинні повторення символу t на одинарні', sep='')
    while True:
        str1 = input('please enter the string: ')
        while True:
            char = input('enter the character to remove: ')
            if len(char) != 1:
                print('only 1 character expected, ', end='')
                continue
            #with different lenghts of char the function will still work, but won't do anything useful
            #it will just return the same string
            #if we want to search for longer char sequences, the function has to be rewritten
            break
        print('Your string before:', str1)
        print('Your string after: ', Compress(str1, char))
        if input('enter q to quit or anything else to run again: ').lower() == 'q':
            break

if __name__ == '__main__':
    main2()