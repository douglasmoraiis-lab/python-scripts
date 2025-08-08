def run(form):
    num1 = float(form.get("num1", 0))
    num2 = float(form.get("num2", 0))
    if num1 > num2:
        return f"O maior número é: {num1}"
    elif num2 > num1:
        return f"O maior número é: {num2}"
    else:
        return "Os números são iguais."