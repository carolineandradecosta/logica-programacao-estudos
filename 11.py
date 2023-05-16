# Desenvolva um programa para calcular a venda de maçãs em uma banca de feira. O cliente compra maçãs custando R
# $1,37 cada uma, mas caso ele compre a partir de uma dúzia pagará com desconto de 10%, portanto o valor da unidade
# ficará por R $1,24. O programa deverá receber o número de maçãs desejadas pelo cliente, e retornar o valor total da
# compra.

def calcula_preco_macas(qtd_maca: int, preco_unidade: float = 1.37, preco_unidade_desconto: float = 1.24):
    if qtd_maca <= 12:
        valor_total = preco_unidade * qtd_maca
        return f'Valor total das maçãs: $ {valor_total}'
    else:
        valor_total = preco_unidade_desconto * qtd_maca
        return f'Valor total das maçãs: $ {valor_total}'


print(calcula_preco_macas(12))
