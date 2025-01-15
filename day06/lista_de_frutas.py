# frutas = ["banana", "maça", "uva", "pera", "manga"]
# # usando o for, para listar cada item que tem dentro de uma lista
# for fruta in frutas:
#     print(fruta)
frutas = []   
while True:
    fruta = input("Digite o nome da fruta ou 'sair' para parar o programa: ")
    if fruta == "sair":
        break
    frutas.append(fruta)
print(frutas)
    