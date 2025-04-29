texto = input("Entre com uma string: ").upper()
contagem = {}

for letra in texto:
    if letra in contagem:
        contagem[letra] +=1
    else:
        contagem[letra] = 1
        
for letra, quantidade in contagem.items():
    print(f"O caractere {letra} aparece {quantidade} vezes")