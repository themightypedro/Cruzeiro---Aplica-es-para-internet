#atividade 2
numero = input('digite um número de três algarismos: ')
inverso = numero[::-1]
soma = int(numero) + int(inverso)
print(f"O inverso do número é: {inverso}")
print(f"A soma é: {numero} + {inverso} = {soma}")