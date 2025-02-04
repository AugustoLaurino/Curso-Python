horarario = input("Digite o horário atual: ")

try:
    hora = int(horarario)

    dia = hora >= 0 and hora <= 11
    tarde = hora >= 12 and hora <= 17
    noite = hora >= 18 and hora <= 23

    if  dia :
        print("Bom dia!")
    elif tarde :
        print("Boa tarde!")
    elif noite :
        print("Boa noite!")
    else :
        print("Não conheço esse horário")
except :
    print("Por favor, digite apenas números inteiros")
