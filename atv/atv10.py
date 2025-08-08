import random

def run(form):
    chute = int(form.get("chute", 0))
    numero_secreto = 5

    if chute == numero_secreto:
        return f"Seu palpite: {chute}\n\n🎉 Parabéns! Você acertou. O número era {numero_secreto}."
    elif chute < numero_secreto:
        return f"Seu palpite: {chute}\n\n❌ Errado! O número secreto é MAIOR. Tente novamente."
    else:
        return f"Seu palpite: {chute}\n\n❌ Errado! O número secreto é MENOR. Tente novamente."