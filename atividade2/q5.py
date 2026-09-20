# Questão 5 - Cadastro de Nomes

# Lista com os 8 nomes de estudantes
nomes = ["Ana", "Carlos", "Guilherme", "Beatriz", "João", "Fernanda", "Leo", "Mariana"]
nomes_longos = []
qtd_longos = 0

print("--- Todos os Nomes ---")
# O 'for' pega um nome de cada vez e guarda na variável 'nome' (no singular)
for nome in nomes:
    print(f"- {nome}")
    
    # Usa len() na variável 'nome' (palavra atual), e NÃO em 'nomes' (lista inteira)
    if len(nome) > 6:
        nomes_longos.append(nome)
        qtd_longos += 1

print("\n--- Nomes com mais de 6 caracteres ---")
for nome in nomes_longos:
    print(f"- {nome}")

print(f"\nTotal de nomes com mais de 6 caracteres: {qtd_longos}")