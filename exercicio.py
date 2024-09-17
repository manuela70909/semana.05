//estrutura de repetição

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero == 5:
        print("Número 5 encontrado, interrompendo o loop.")
        break
    print(f"Número atual: {numero}")


//estrutura de decisão

numero = 5

if numero > 5:
    print("O número é maior que 5.")
elif numero == 5:
    print("O número é igual a 5.")
else:
    print("O número é menor que 5.")
