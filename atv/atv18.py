idade = int(input("Digite a idade da criança: "))

if idade >= 0 and idade <= 3:
    print("Berçário")
elif idade >= 4 and idade <= 5:
    print("Pré-escola")
elif idade >= 6 and idade <= 10:
    print("Ensino Fundamental I")
else:
    print("Fora da faixa")
