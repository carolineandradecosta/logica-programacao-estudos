
def calcula_imc(peso: float, altura: float):
    imc = peso / altura ** 2
    if imc < 18.5:
        print(f'IMC = {imc} - abaixo do peso')
    elif 18.5 <= imc < 25.0:
        print(f'IMC = {imc} - peso normal')
    elif 25 <= imc < 30:
        print(f'IMC = {imc} - acima do peso')
    elif imc >= 30.0:
        print(f'IMC = {imc} - obeso')


calcula_imc(55.0, 1.61)
