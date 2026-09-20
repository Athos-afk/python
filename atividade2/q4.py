# Questão 4 - Lista de Notas

notas = [7.5, 8.0, 6.5, 9.0, 5.5, 8.5]

soma_notas = 0
acima_ou_igual_7 = 0

print("--- Notas dos Estudantes ---")
# O 'for' percorre cada elemento da lista e guarda na variável 'nota' (no singular)
for nota in notas:
    print(f"Nota: {nota}")
    soma_notas = soma_notas + nota  # Soma a nota individual, e não a lista inteira
    
    if nota >= 7.0:
        acima_ou_igual_7 += 1

# Calcula a média da turma
media = soma_notas / len(notas)

print(f"\nMédia da turma: {media:.2f}")
print(f"Quantidade de estudantes com nota >= 7.0: {acima_ou_igual_7}")