# Gerenciar um estoque para a empresa U não é complicado, mas ele te pediu para desenvolver um programa para realizar
# esta tarefa. Ela precisa que o usuário informe a quantidade máxima e mínima do estoque do produto X, e também a
# quantidade real existente no estoque. Por fim, o programa deve responder se é necessário adquirir mais produtos,
# comparando o estoque real com a média entre valor máximo e mínimo.
# a. se o estoque real estiver abaixo da média, informar a necessidade de compra;
# b. se estiver acima da média informar que não precisa adquirir novos produtos;
# c. se estiver na média, informa que em breve será necessária nova aquisição de produtos;


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
