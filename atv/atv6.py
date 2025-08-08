def run(form):
    num = int(form.get("num", 0))
    resultado_tabuada = []
    for i in range(1, 11):
        resultado = num * i
        resultado_tabuada.append(f"{num} x {i} = {resultado}")
    return "\n".join(resultado_tabuada)