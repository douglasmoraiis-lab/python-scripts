def run(form):
    nota1 = float(form.get("nota1", 0))
    nota2 = float(form.get("nota2", 0))
    nota3 = float(form.get("nota3", 0))
    media = (nota1 + nota2 + nota3) / 3
    
    resultado = f"Sua média é: {media:.2f}\n"
    if media >= 7:
        resultado += "Parabéns, você foi Aprovado!"
    else:
        resultado += "Ops, você foi Reprovado! Tente novamente."
    return resultado