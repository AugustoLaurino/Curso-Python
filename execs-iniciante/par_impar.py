num = input("Digite um numero inteiro: ")

try :
   num_float = float(num)
   par_impar = num_float % 2 == 0
   par_impar_texto = "ímpar"

   if par_impar :
      par_impar_texto = "par"
      
   print(f"O numero {num_float} é {par_impar_texto}")
except :
    print("Você não digitou um numero inteiro")