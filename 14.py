
def operacoes_aritmeticas(numero_1: float, numero_2: float, simbolo_operacao: str):
    if simbolo_operacao == "+":
        soma = numero_1 + numero_2
        print(f'Soma = {soma}')
    elif simbolo_operacao == "-":
        subtracao = numero_1 - numero_2
        print(f'Subtração = {subtracao}')
    elif simbolo_operacao == "*":
        multiplicacao = numero_1 * numero_2
        print(f'Multiplicação = {multiplicacao}')
    elif simbolo_operacao == "/":
        divisao = numero_1 / numero_2
        print(f'Divisão = {divisao}')
    elif simbolo_operacao == "**":
        potenciacao = numero_1 ** numero_2
        print(f'Potenciação = {potenciacao}')

operacoes_aritmeticas(10,10,"+")
operacoes_aritmeticas(10,5,"-")
operacoes_aritmeticas(5,5,"*")
operacoes_aritmeticas(10,2,"/")
operacoes_aritmeticas(5,2,"**")
