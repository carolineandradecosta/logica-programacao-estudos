# Exercício do IMC (Índice de Massa Corporal): Escreva um programa em Python que solicite ao usuário sua altura em
# metros e seu peso em quilogramas. Calcule o Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / (altura *
# altura). Exiba o resultado do IMC na tela.


def calcula_imc(altura: float, peso: float):
    imc = (peso / (altura * altura)).__round__(2)
    return f'O seu Índice de Massa Corporal é: {imc}'

print(calcula_imc(1.61, 55.0))