alturas = [1.62, 1.70, 1.59, 1.67, 1.78, 1.80, 1.58, 1.75, 1.74, 1.79, 1.81, 1.55, 1.64, 1.65, 1.71]


def menor_e_maior_altura(altura):
    menor_altura = min(altura)
    maior_altura = max(altura)
    print(f'menor altura = {menor_altura}')
    print(f'maior altura = {maior_altura}')


menor_e_maior_altura(alturas)
