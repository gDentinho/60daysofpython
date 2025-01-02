
def verificando_numero_par():
    while True:
        try:
            entrada = input("Digite um numero: ")
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} par!")
            else:
                print(f"{numero} ímpar!")
        except ValueError:
            print(f"Você nao digitou um numero inteiro.")
        
verificando_numero_par()
