nome = input("Digite seu primeiro nome: ")
tam_nome = len(nome)
try :
    if tam_nome <= 4:
        print("Seu nome é curto")
    elif tam_nome >= 5 and tam_nome <= 6 :
        print("Seu nome é normal")
    elif tam_nome > 6 :
        print("Seu nome é muito grande")
except : 
    print("Digite um nome válido")