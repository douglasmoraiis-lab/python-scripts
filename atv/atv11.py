def run(form):
    try:
        idade = int(form.get("idade", 0))
        if idade >= 18:
            return "Você é MAIOR de idade."
        else:
            return "Você é MENOR de idade."
    except ValueError:
        return "Erro: Por favor, digite um número válido para a idade."