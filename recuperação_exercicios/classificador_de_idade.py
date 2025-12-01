idade = int(input("Digite sua idade: "))

if idade < 12:
    print("criança")
elif 12 <= idade <= 17:
    print("adolescente")
elif 18 <= idade <= 59:
    print("adulto")
else:
    print("idoso")
