def run(form):
    nome = form.get("nome", "Visitante")
    return f"Olá, {nome}! Bem-vindo ao programa."