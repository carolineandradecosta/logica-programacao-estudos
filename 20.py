''' Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu primeiro nome, o
sobrenome, a idade e a cidade em que ela vive. Você deverá ter chaves como primeiro_nome, sobrenome, idade, e cidade.
Por fim, mostre cada informação armazenada em seu dicionário. '''


glosario_nome = {
    'primeiro_nome': 'caroline',
    'segundo_nome': 'andrade',
    'idade': '31',
    'cidade': 'campina grande'
}

for chave in glosario_nome:
    print(f'{chave}: {glosario_nome[chave]}')
