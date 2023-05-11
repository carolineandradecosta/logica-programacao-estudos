# Exercício do Desconto: Escreva um programa em Python que solicite ao usuário o valor de um produto e o percentual de
# desconto. Calcule o valor do desconto e exiba o valor final após o desconto.

valor_produto = float(input("Informe o valor do produto: "))
valor_desconto = float(input("Informe o percentual de desconto: "))

valor_desconto = valor_desconto / 100

desconto = valor_produto * valor_desconto

valor_final_produto = valor_produto - desconto

print(f'Valor do produto: {valor_produto} \n'
      f'Valor do desconto: {valor_desconto}\n'
      f'Desconto: {desconto}%\n'
      f'Produto com desconto: {valor_final_produto}')
