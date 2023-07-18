
def menu():
    menu = '''
    [d] Digite d para depositar
    [s] Digite s para sacar
    [e] Digite e para extrato
    [sair] Digite sair para fechar o sistema
    '''
    return input(f"Informe a opção desejada {menu}")

def depositar(saldo,valor,extrato):

    if valor > 0:
        saldo += int(valor)
        extrato+= f'Deposito realizado no valor de R${valor}'
        return saldo,valor

def saque(saldo,valorsaque, extrato, numero_saques, limite,LIMITE_SAQUES):
    if valorsaque > 0:
        if saldo < valorsaque:
            return "Não é possivel sacar , saldo insuficiente"
        elif valorsaque > limite:
            return"Não é possivel sacar um valor acima de R$ 500,00"
        elif numero_saques == LIMITE_SAQUES:
            return "Voce excedeu o limite maximo de saques diarios"
        else:
            saldo -= int(valorsaque)
            extrato += f'Deposito realizado no valor de R${valorsaque}'
        return saldo,valorsaque,extrato
    else:
        return "Não é possivel sacar um numero negativo"
def main():

 saldo = 0
 limite = 500
 numero_saques = 0
 LIMITE_SAQUES = 3
 extrato =f'Operacao realizada'
 opcao= menu()
 while True:
            #opcao = input(menu)
        if opcao == "d":
                valor = int(input("Informe o valor do deposito R$"))
                saldo,valor= depositar(saldo,valor, extrato)
                print(f"Depósito realizado com sucesso no valor de : R${valor} ")
                opcao = menu()
        if opcao == "s":
            valorsaque = int(input("Informe o valor do saque :"))
            result =saque(saldo,valorsaque, extrato, numero_saques, limite,LIMITE_SAQUES)
            '''print(f"Saque realizado com sucesso no valor de : R${valorsaque} ")'''
            print(result)
            opcao = menu()

        if opcao == "e":
            print(f"""Extrato da sua conta :
             saldo R${saldo} sua conta permite {LIMITE_SAQUES}
             numeros de saques você já realizou 
             {numero_saques} saques
            Veja o histórico:
       Primeiro Saque no valor de R$ {dados['saque1']:.2f} reais
        Segundo Saque no valor de R$ {dados['saque2']:.2f} reais
        Terceiro Saque no valor de R$ {dados['saque3']:.2f} reais""")
            continue
        if opcao == "sair":
            print('Fechando o sistema')
            break
        else:
            print("Opção inválida")

main()

'''  {
        "saque1": 0,
        "saque2": 0,
        "saque3": 0
}
 if numero_saques == 0:
                    dados['saque1'] = valorsaque
                if numero_saques == 1:
                    dados['saque2'] = valorsaque
                if numero_saques == 2:
                    dados['saque3'] = valorsaque
                    numero_saques += 1
                    print(f"Saque no valor de R${valorsaque} realizado com sucesso")
                    continue


'''