# Verifica o tipo de diária e calcula o valor total
tipo_diaria = input("Digite o tipo de diária: ")
quantidade_diaria = int(input("Digite a quantidade de diárias desejadas: "))
valor_diaria = 0
if tipo_diaria == 'S':
    valor_total = 255.50 * quantidade_diaria
elif tipo_diaria == 'D':
    valor_total = 305.50 * quantidade_diaria
elif tipo_diaria == 'T':
    valor_total = 360.50 * quantidade_diaria
else:
    valor_total = valor_diaria  # Indica que o tipo de diária é inválido

# Exibe o resultado
if valor_total is None:
    print("Tipo de diária inválido")
else:
    print(f"O valor total a pagar é: R${valor_total:.2f}")