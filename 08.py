# Exercício da Conversão de Moedas: Escreva um programa em Python que solicite ao usuário um valor em Real (BRL) e
# faça a conversão desse valor para Dólar Americano (USD). Considere a taxa de câmbio fixa de 1 USD = 5 BRL. Exiba o
# valor convertido na tela.

def converteRealEmDolar (valorReal: float, cambioDolar: float = 5.0) :
    valorConvertidoDolar = valorReal / cambioDolar
    return (f'Valor em Dólar: {valorConvertidoDolar} USD')

print(converteRealEmDolar(50.0))
