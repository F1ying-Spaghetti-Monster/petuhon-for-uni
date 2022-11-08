from string import ascii_lowercase
#ascii_lowercase can be defined without imports, but it's more convenient to do this

print('Лабораторна робота #4 Савчук Іван варіант #21')

while True:
    print('Завдання 1: створити рядок із літер, яких немає у рядках str1 та str2')

    str1 = input('please enter first string: ')
    str2 = input('please enter second string: ')

    letters_set = set((str1 + str2).lower())
    #strings are converted to lowercase and turned into a set of unique characters
    #if we want to optimize memory usage, we can add a check and only add letters into the set

    str3 = ''
    for i in ascii_lowercase:
        if i not in letters_set:
            str3 += i
    #we can also ditch the set and just check like this: if i not in str1 and i not in str2
    #this will be more efficient for memory, but less efficient for performance

    #when passed empty strings, program runs correctly and returns all letters of the alphabet
    print('string of other letter:', str3)
    if input('enter q to exit, or anything else to run again: ').lower() == 'q':
        break