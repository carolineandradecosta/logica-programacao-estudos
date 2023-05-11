# Exercício da Conversão de Temperatura: Escreva um programa em Python que solicite ao usuário uma temperatura em
# graus Celsius e faça a conversão para Fahrenheit. Exiba o resultado na tela.

tem_celsius = float(input("Informe a temperatura em graus Celsius: "))

temp_fahrenheit = (tem_celsius * 1.8) + 32

print(f'A temperatura em Celcius é {tem_celsius}')
print(f'A temperatura em Fahrenheit é {temp_fahrenheit}')