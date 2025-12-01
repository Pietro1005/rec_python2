qtd = int(input("Quantos alunos serão cadastrados? "))

nomes = []
notas = []

for _ in range(qtd):
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))
    
    nomes.append(nome)
    notas.append(nota)

print("\n=== TODOS OS ALUNOS ===")
for i in range(qtd):
    print(f"{nomes[i]} - Nota: {notas[i]}")

print("\n=== APROVADOS (nota >= 7) ===")
for i in range(qtd):
    if notas[i] >= 7:
        print(f"{nomes[i]} - Nota: {notas[i]}")
