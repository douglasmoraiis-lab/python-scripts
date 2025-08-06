#Peça um número e mostre a tabuada dele de 1 a 10.
num = int(input("Digite um número para ver a tabuada:"))
for i in range(1, 11):
    resultado = num * i 
    print(f"{num} x {i} = {resultado}")