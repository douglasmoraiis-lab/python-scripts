def run(form):
    # A senha correta é o número 1234
    senha_correta = "1234"
    senha_digitada = form.get("senha")
    
    if senha_digitada == senha_correta:
        return "ACESSO PERMITIDO"
    else:
        return "ACESSO NEGADO"