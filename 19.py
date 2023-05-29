''' Faça um programa que mostre as tabuadas dos números de 1 a 10. '''

for x in range(1, 11):
    print(f'\nTabuada do {x}')
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')
