qtd = int(input("Quantos números você quer informar? "))

numeros = []

for _ in range(qtd):
    n = float(input("Digite um número: "))
    numeros.append(n)

maior = max(numeros)
menor = min(numeros)

print("\nMaior número:", maior)
print("Menor número:", menor)
