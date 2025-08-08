# Leia uma letra do alfabeto e diga se é uma vogal ou consoante.

Letra = input("Digite uma letra do alfabeto: ").lower()
if Letra in "aeiou":
  print("A letra é uma vogal.")
else:
  print("A letra é uma consoante.")