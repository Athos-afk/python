def cadastrar_cliente(clientes):

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    telefone = input("Digite o telefone: ")

    cliente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")


def pesquisar_cliente(clientes):

    nome_pesquisa = input("Digite o nome do cliente: ").lower()

    encontrado = False

    for cliente in clientes:

        if cliente["nome"].lower() == nome_pesquisa:

            print("\nCliente encontrado:")
            print(f"Nome: {cliente['nome']}")
            print(f"Idade: {cliente['idade']}")
            print(f"Telefone: {cliente['telefone']}")

            encontrado = True

    if not encontrado:
        print("Cliente não encontrado.")


def listar_clientes(clientes):

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    print("\n--- Clientes cadastrados ---")

    for cliente in clientes:

        print(f"Nome: {cliente['nome']}")
        print(f"Idade: {cliente['idade']}")
        print(f"Telefone: {cliente['telefone']}")
        print("--------------------")


clientes = []

while True:

    print("\n--- MENU ---")
    print("1 - Cadastrar cliente")
    print("2 - Pesquisar cliente")
    print("3 - Listar clientes")
    print("4 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente(clientes)

    elif opcao == "2":
        pesquisar_cliente(clientes)

    elif opcao == "3":
        listar_clientes(clientes)

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
