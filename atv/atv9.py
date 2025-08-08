def run(form):
    palavra = form.get("palavra", "").lower()
    if not palavra:
        return "Por favor, digite uma palavra."
        
    vogais = "aeiou"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return f"A palavra '{palavra}' tem {contador} vogais."