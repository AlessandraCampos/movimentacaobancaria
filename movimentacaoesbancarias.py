menu='''
[d] Digite d para depositar
[s] Digite s para sacar
[e] Digite e para extrato
[sair] Digite sair para fechar o sistema
'''

saldo=0
limite=500
numero_saques=0
LIMITE_SAQUES=3
dados= {
    "saque1":0,
    "saque2":0,
    "saque3":0
}

while True:
    opcao = input(menu)
    if opcao == "d":
        valordodeposito = input("Informe o valor do deposito R$")
        if valordodeposito > 0:
            saldo += int(valordodeposito)
            print(f"Depósito no valor de : R${valordodeposito}")
            continue
    if opcao == "s":
        valorsaque = int(input("Informe o valor do saque :"))
        if saldo < valorsaque:
            print("Não é possivel sacar , saldo insuficiente")
        elif valorsaque > 500:
            print("Não é possivel sacar um valor acima de R$ 500,00")
            continue
        elif numero_saques == 3:
            print("Voce excedeu o limite maximo de saques diarios")
            continue
        elif valorsaque > 0:
            saldo -= int(valorsaque)
            if numero_saques == 0:
                dados['saque1'] = valorsaque
            if numero_saques == 1:
                dados['saque2'] = valorsaque
            if numero_saques == 2:
                dados['saque3'] = valorsaque
                numero_saques += 1
                print(f"Saque no valor de R${valorsaque} realizado com sucesso")
                continue
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
        break
    else:
        print("Opção inválida")

