import random

# O estado do jogo (número secreto, tentativas) precisa ser gerenciado.
# Esta é uma implementação SIMPLES que reinicia o jogo a cada palpite.
# Uma versão completa exigiria sessões Flask para manter o estado.
def run(form):
    chute = int(form.get("chute", 0))
    
    # Para este exemplo simples, vamos gerar um número fixo para testar.
    # Em uma aplicação real, você precisaria de uma forma de lembrar o número.
    numero_secreto = 5 # Vamos fixar para simplificar
    
    if chute == numero_secreto:
        return f"Seu palpite: {chute}\n\n🎉 Parabéns! Você acertou. O número era {numero_secreto}."
    elif chute < numero_secreto:
        return f"Seu palpite: {chute}\n\n❌ Errado! O número secreto é MAIOR. Tente novamente."
    else:
        return f"Seu palpite: {chute}\n\n❌ Errado! O número secreto é MENOR. Tente novamente."