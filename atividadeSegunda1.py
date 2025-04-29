email = input("Entre com o seu e-mail: ")
dominio = email.split('@')[1]
print(f"O domínio do seu e-mail é: http://{dominio}")