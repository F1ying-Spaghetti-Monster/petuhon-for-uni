def cartesian_product(A, B):
    C = set()
    for i in A:
        for j in B:
            C.add((i, j))
    return C

def main2():
    Un = {1, 2, 3, 4, 'a', 'b', 'c', 'd', 'ee', 'tt', 'ww'}
    setA = {1, 'a', 'b', 'ww', 2, 'd'}
    setB = {2, 'a', 'b', 'ee', 1, 3}
    setC = {}

    print('\nЗавдання 2, провести операції над множинами')
    print(f'Univ.= {Un}\nset A= {setA}\nset B= {setB}\n')

    setC = setA.union(setB)
    print(f'A ∪ B = {setC}')

    setC = setA & setB
    print(f'A ∩ B = {setC}')

    setC = setA - setB
    print(f'A \ B = {setC}')

    setC = setB - setA
    print(f'B \ A = {setC}')

    setC = setA ^ setB
    print(f'A ^ B = {setC}')

    setC = Un - setA
    print(f'¬A = {setC}')

    setC = Un - setB
    print(f'¬B = {setC}')

    setC = setC = cartesian_product(setA, setB)
    print(f'\nA x B  = {setC}\n')

    setC = cartesian_product(setB, setA)
    print(f'B x A  = {setC}\n')

    setC = setA.union(setB) & (Un - setA)
    print(f'F = ((A∪B)∩(¬A)) = {setC}\n')
    
    input('press enter to exit')

if __name__ == '__main__':
    main2()