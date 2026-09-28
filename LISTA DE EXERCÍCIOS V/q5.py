def validar_senha(senha):

    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True

    if tem_maiuscula and tem_minuscula and tem_numero:
        return True

    return False


while True:

    senha = input("Digite uma senha: ")

    if validar_senha(senha):
        print("Senha válida!")
        break
    else:
        print("Senha inválida!")
        print("A senha deve possuir:")
        print("- Pelo menos 8 caracteres")
        print("- Uma letra maiúscula")
        print("- Uma letra minúscula")
        print("- Um número")
