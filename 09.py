# Exercício do Volume de uma Esfera: Escreva um programa em Python que solicite ao usuário o raio de uma esfera.
# Calcule o volume dessa esfera usando a fórmula V = (4/3) * pi * r³, onde pi é uma constante aproximada de 3.1415.
# Exiba o volume calculado na tela.

import numpy


def calcula_volume(raio: float):
    pi = numpy.pi
    volume = ((4 / 3) * pi * (raio ** 3)).__round__(2)
    return f'Volume de uma Esfera de raio {raio} = {volume}'


print(calcula_volume(2.0))

