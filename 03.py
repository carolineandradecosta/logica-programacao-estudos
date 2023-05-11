# Exercício da Média: Escreva um programa em Python que solicite ao usuário duas notas e calcule a média entre elas. Em
# seguida, exiba o resultado na tela.

# nota_1 = float(input("Informe a nota 1: "))
# nota_2 = float(input("Informe a nota 2: "))
#
# media = (nota_1 + nota_2) / 2
#
# print(f'Sua média é {media}')

# Outra forma de resolver, escrevendo uma função:
def calcula_media(nota1, nota2):
    return (nota1 + nota2) / 2

print(calcula_media(10.0, 8.0))