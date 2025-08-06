#Peça dois números e diga qual é o maior, ou se são iguais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2 :
  print(f"O maior número é: {num1}")
elif num2 > num1:
  print(f" O maior número é: {num2}")
else: 
  print(f"Os números são iguais.")