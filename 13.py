
def gerencia_estoque(qtd_max: int, qtd_min: int, qtd_real: int):
    media = (qtd_max + qtd_min) / 2

    if qtd_real < media:
        print(f'Estoque abaixo da média, necessário realizar compra')
    elif qtd_real > media:
        print(f'Estoque acima da média, não é necessário realizar compra')
    else:
        print(f'Em breve será necessário comprar novos produtos')

gerencia_estoque(100, 20, 110)
gerencia_estoque(100, 20, 50)
gerencia_estoque(100, 20, 60)