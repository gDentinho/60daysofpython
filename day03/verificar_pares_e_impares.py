def verificar_numero_par():
    numero = int(input("Digite um numero para verificar se ele é par ou impar: "))
    if numero % 2 == 0:
        print(f"{numero} é par!")
    else:
        print(f"{numero} é ímpar")
        
verificar_numero_par()
