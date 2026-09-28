def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")


def listar_tarefas(tarefas):

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\n--- Tarefas ---")

        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")


def remover_tarefa(tarefas):

    listar_tarefas(tarefas)

    if len(tarefas) > 0:

        numero = int(input("Digite o número da tarefa que deseja remover: "))

        if 1 <= numero <= len(tarefas):
            tarefas.pop(numero - 1)
            print("Tarefa removida com sucesso!")
        else:
            print("Número inválido.")


tarefas = []

while True:

    print("\n--- MENU ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa(tarefas)

    elif opcao == "2":
        listar_tarefas(tarefas)

    elif opcao == "3":
        remover_tarefa(tarefas)

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
