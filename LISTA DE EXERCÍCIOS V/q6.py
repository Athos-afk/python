def calcular_total(produtos):
    total = 0

    for produto in produtos:
        total += produto["quantidade"] * produto["preco"]

    return total


carrinho = []

while True:

    nome = input("Digite o nome do produto: ")

    quantidade = int(input("Digite a quantidade: "))

    preco = float(input("Digite o preço: R$ "))

    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    carrinho.append(produto)

    continuar = input("Deseja adicionar outro produto? (s/n): ").lower()

    if continuar != "s":
        break


print("\n--- Carrinho de Compras ---")

for produto in carrinho:
    subtotal = produto["quantidade"] * produto["preco"]

    print(f"Produto: {produto['nome']}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print()


total = calcular_total(carrinho)

print(f"Valor total da compra: R$ {total:.2f}")
