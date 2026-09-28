def autenticar(usuario, senha):
    usuario_correto = "admin"
    senha_correta = "1234"

    if usuario == usuario_correto and senha == senha_correta:
        return True
    else:
        return False


tentativas = 0
acesso = False

while tentativas < 3:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if autenticar(usuario, senha):
        print("Acesso autorizado!")
        acesso = True
        break
    else:
        tentativas += 1
        print("Usuário ou senha incorretos.")

if not acesso:
    print("Acesso bloqueado. Você excedeu o limite de tentativas.")
