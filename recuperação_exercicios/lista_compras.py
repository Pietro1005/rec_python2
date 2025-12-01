lista = []

while True:
    item = input("Digite um item para a lista (ou 'fim' para encerrar): ")

    if item.lower() == "fim":
        break

    lista.append(item)

print("\nLista de compras:")
for i in lista:
    print("-", i)
