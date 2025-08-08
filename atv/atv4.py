def run(form):
    num = int(form.get("num", 0))
    if num % 2 == 0:
        return f"O número {num} é PAR."
    else:
        return f"O número {num} é ÍMPAR."