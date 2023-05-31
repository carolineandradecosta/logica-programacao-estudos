''' Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram
no conjunto dos números de 1 até 500. '''

soma: int = 0
for numero in range(1, 500):
    if numero % 2 == 1 and numero % 3 == 0:
        soma += numero

print(f'Soma = {soma}')
