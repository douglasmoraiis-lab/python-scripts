def run(form):
    try:
        ano = int(form.get("ano", 0))
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            return f"O ano de {ano} É um ano bissexto."
        else:
            return f"O ano de {ano} NÃO é um ano bissexto."
    except ValueError:
        return "Erro: Por favor, digite um ano válido."