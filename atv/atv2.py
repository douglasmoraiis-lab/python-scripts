def run(form):
    num1 = float(form.get("num1", 0))
    num2 = float(form.get("num2", 0))
    soma = num1 + num2
    return f"A soma de {num1} + {num2} é: {soma}"