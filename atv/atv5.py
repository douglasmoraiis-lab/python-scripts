def run(form):
    num = int(form.get("num", 0))
    resultado = []
    for i in range(1, num + 1):
        resultado.append(f"Contando: {i}")
    return "\n".join(resultado)