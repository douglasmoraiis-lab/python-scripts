#O computador escolhe um número de 1 a 10 e o usuário tenta adivinhar até acertar.# Questão 10 - Jogo de Adivinhação

import random

# O computador escolhe um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)
tentativas = 0

print("=== Jogo de Adivinhação ===")
print("Tente adivinhar o número entre 1 e 10!\n")

while True:
    chute = int(input("Digite seu palpite: "))
    tentativas += 1

    if chute == numero_secreto:
        print(f"\n🎉 Parabéns! Você acertou em {tentativas} tentativa(s).")
        
    else:
        print("❌ Errado! Tente novamente.")
