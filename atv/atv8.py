#Peça 3 notas e calcule a média.
#Caso contrário, exiba "Reprovado".

nota1 = float(input("Digite a Primeira nota: "))
nota2 = float(input("Digite a Segunda nota: "))
nota3 = float(input("Digite a Terceira nota: "))

media = (nota1 + nota2 + nota3) /3

print(f"\nSua média é: {media:.2f}")

if media >= 7:
  print("Parabéns, você foi Aprovado")
else:
  print("Ops, você foi Reprovado! Tente novamente")