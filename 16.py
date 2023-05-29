# Lista inicial
lista_convidados = ["Hermione", "Harry Potter", "Ron"]
print(f'Lista inicial: {lista_convidados}')

def adiciona_e_remove_convidado(lista: list, operacao: str, pessoa: str, posicao: str):
    if operacao == "-":
        lista.remove(pessoa)
        print(f'{pessoa} será retirado da lista {lista}')
    elif operacao == "+":
        if posicao == "inicio":
            lista.insert(0, pessoa)
            print(f'{pessoa} foi adicionado ao início da lista: {lista}')
        elif posicao == "meio":
            meio_lista = int((len(lista)) / 2)
            lista.insert(meio_lista, pessoa)
            print(f'{pessoa} foi adicionado ao meio da lista: {lista}')
        elif posicao == "final":
            lista.insert((len(lista)), pessoa)
            print(f'{pessoa} foi adicionado ao final da lista: {lista}')


adiciona_e_remove_convidado(lista_convidados, "+", "Dobby", "inicio")
adiciona_e_remove_convidado(lista_convidados, "+", "Rúbeo Hagrid", "meio")
adiciona_e_remove_convidado(lista_convidados, "+", "Albus Dumbledore", "final")
adiciona_e_remove_convidado(lista_convidados, "-", "Dobby", "final")
