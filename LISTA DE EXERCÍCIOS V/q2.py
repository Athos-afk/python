def cadastrar_produto(produtos, nome, preco):
    produtos[nome] = preco


produtos = {}

while True:
    nome = input("Digite o nome do produto: ")

    while True:
        preco = float(input("Digite o preço do produto: R$ "))

        if preco > 0:
            break

        print("O preço deve ser maior que zero.")

    cadastrar_produto(produtos, nome, preco)

    continuar = input("Deseja cadastrar outro produto? (s/n): ").lower()

    if continuar != "s":
        break


print("\nProdutos cadastrados:")

for nome, preco in produtos.items():
    print(f"{nome}: R$ {preco:.2f}")
