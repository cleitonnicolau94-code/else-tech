
import os

pasta = os.path.dirname(os.path.abspath(__file__))

clientes = []

if os.path.exists(os.path.join(pasta, "clientes.txt")):
    arquivo = open(os.path.join(pasta, "clientes.txt"), "r")

    for linha in arquivo:
        dados = linha.strip().split("|")
        clientes.append(dados)

    arquivo.close()

while True:

    print("================================")
    print("   CLEITON SUPORTE TÉCNICO      ")
    print("================================")
    print("1 - Cadastrar Clientes")
    print("2 - Listar Clientes")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")
    print("Você escolheu", opcao)
    if opcao == "1":
        id_cliente = len(clientes) + 1
        nome = input("Nome do cliente: ")
        telefone = input("Telefone do cliente: ")
        equipamento = input("Equipamento: ")

        clientes.append([id_cliente, nome, telefone, equipamento])

        pasta = os.path.dirname(os.path.abspath(__file__))
        arquivo = open(os.path.join(pasta, "clientes.txt"), "a")
        arquivo.write(str(id_cliente) + "|" + nome + "|" + telefone + "|" + equipamento + "\n")
        arquivo.close()

        print()
        print("===== CLIENTE CADASTRADO =====")
        print("Nome:", nome)
        print("Telefone:", telefone)
        print("Equipamento:", equipamento)
        
    elif opcao == "2":
        print("===== LISTA DE CLIENTES =====")
        for cliente in clientes:
            print("ID:", cliente [0])
            print("Nome:", cliente[1])
            print("Telefone:", cliente[2])
            print("Equipamento:", cliente[3])
            print()

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção invalída.") 