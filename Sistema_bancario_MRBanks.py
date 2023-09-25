saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
valor_saque = 0
valor_deposito = 0

menu = """
    ===========  MENU  ============
    Olá Bem-vindo cliente MR Banks,
    é sempre um prazer te-lo com
    a gente.
    Mais que um banco, uma família!
    =============================== 

    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair

===============================

Obrigado por ser nosso cliente."""
extrato = f"""
=========  EXTRATO  ===========
Aqui constam suas últimas 
movimentações financeiras, se
tiver dúvidas entre em contato.
===============================
Saldo : {saldo}
Limite : {limite}
"""
print (menu)

opcao = input("Selecione uma opção :")
while True:
    if opcao == '1':
        print("Depósito")
        valor_deposito = input("Digite o valor a ser depositado")

    elif opcao == "2":
        print("Saque")
        valor_saque = input("Digite o valor a ser retirado")

    elif opcao == "3":
        print("Extrato")
        print(extrato)
    elif opcao == "0":
        print("Agradecemos a sua visita, volte sempre !")
        break
    
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
print(menu)
