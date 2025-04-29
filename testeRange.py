num = int(input('digite um número: '))
qt = len(str(num))
print(qt)

string = input('digite um texto: ')
inversa = " "
for x in string:
    inversa = x + inversa
print(inversa)

fruit = "banana"
print(fruit[0:-2])

texto = input('digite um texto: ')
pontuacao = [".", "," , ", " , "," , ";" , ":" , "?"]

#remove os sinais de pontuação
for p in pontuacao:
    texto = texto.replace(p," ")
    
#split devolve lista com palavras como itens
numero_palavras = len(texto.split())
print("Número de palavras:" , numero_palavras)