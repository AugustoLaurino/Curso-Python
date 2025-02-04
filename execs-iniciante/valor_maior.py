primeiroValor = input("Digite um valor: ")
segundoValor = input("Digite outro valor: ")

if primeiroValor > segundoValor :
    print(f"primeiroValor = '{primeiroValor}' é maior do que o segundoValor = '{segundoValor}'")
elif primeiroValor < segundoValor :
    print(f"segundoValor= '{segundoValor}' é maior do que o primeiroValor = '{primeiroValor}'")
elif primeiroValor == segundoValor:
    print("Os números são iguais")