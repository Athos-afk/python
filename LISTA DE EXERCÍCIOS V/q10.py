def cadastrar_estudante(estudantes):

    nome = input("Digite o nome do estudante: ")
    nota = float(input("Digite a nota do estudante: "))

    estudante = {
        "nome": nome,
        "nota": nota
    }

    estudantes.append(estudante)

    print("Estudante cadastrado com sucesso!")


def calcular_media(estudantes):

    if len(estudantes) == 0:
        return 0

    total = 0

    for estudante in estudantes:
        total += estudante["nota"]

    return total / len(estudantes)


def listar_estudantes(estudantes):

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    print("\n--- Estudantes ---")

    for estudante in estudantes:

        if estudante["nota"] >= 7:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        print(f"Nome: {estudante['nome']}")
        print(f"Nota: {estudante['nota']:.2f}")
        print(f"Situação: {situacao}")
        print("--------------------")


def mostrar_media(estudantes):

    media = calcular_media(estudantes)

    print(f"Média geral da turma: {media:.2f}")


estudantes = []

while True:

    print("\n--- MENU ---")
    print("1 - Cadastrar estudante")
    print("2 - Listar estudantes")
    print("3 - Mostrar média geral")
    print("4 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_estudante(estudantes)

    elif opcao == "2":
        listar_estudantes(estudantes)

    elif opcao == "3":
        mostrar_media(estudantes)

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
