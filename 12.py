# Um programa é necessário para habilitar o funcionamento de uma conta corrente em um banco digital. O programa deve
# permitir ao cliente iniciar com um depósito, realizar um saque, e ao final verificar se o saldo da conta está
# positivo ou negativo. Se negativo, informa qual o valor será necessário para quitar o débito.

def calcula_saldo(deposito: float, saque: float):
    saldo: float = 0.0
    saldo += deposito
    if saque > saldo:
        debito = saque - saldo
        return f'Saldo negativo de: -{debito}'
    else:
        saldo -= saque
        return f'Saldo positivo de: {saldo}'


print(calcula_saldo(500.0, 200.0))
