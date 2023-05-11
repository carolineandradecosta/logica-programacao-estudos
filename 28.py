# [FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C), sendo
# que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raízes reais).

# a = int(input("Informe o valor de a: "))
# b = int(input("Informe o valor de b: "))
# c = int(input("Informe o valor de c: "))
#
# x1 = (- b + (b**2 - (4 * a * c))**(1/2)) / (2 * a)
# x2 = (- b - (b**2 - (4 * a * c))**(1/2)) / (2 * a)

# print(x1)
# print(x2)

def calcula_raizes(a, b, c):
    if a == 0:
        print(f'a = 0, a equação não é do segundo grau')
    else:
        delta = b**2 - (4 * a * c)

        if delta < 0:
            print(f'Não existe reizes reais')
        elif delta == 0:
            raiz = - b / (2 * a)
            print(f'O delta é igual a zero, raiz = {raiz}')
        else:
            x1 = (- b + (delta ** (1/2))) / (2 * a)
            x2 = (- b - (delta ** (1/2))) / (2 * a)
            print(f'Primeira raiz = {x1}')
            print(f'Segunda raiz = {x2}')

calcula_raizes(4,-2,-6)