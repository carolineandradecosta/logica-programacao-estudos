# Exercício do Tempo de Viagem: Escreva um programa em Python que solicite ao usuário a distância de uma viagem (em
# km) e a velocidade média (em km/h). Calcule o tempo de viagem em horas e exiba o resultado.

def calculaTempoViagem (distancia: float, velocidadeMedia: float) :
    tempoViagem = (distancia / velocidadeMedia)
    return tempoViagem

print(f'O tempo da viagem, em horas: {calculaTempoViagem(100.0, 60.0):0.2f}')
