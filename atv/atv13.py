def run(form):
    letra = form.get("letra", "").lower()
    if len(letra) != 1 or not letra.isalpha():
        return "Erro: Por favor, digite uma única letra do alfabeto."

    if letra in "aeiou":
        return f"A letra '{letra}' é uma VOGAL."
    else:
        return f"A letra '{letra}' é uma CONSOANTE."