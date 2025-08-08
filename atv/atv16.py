def run(form):
    try:
        idade = int(form.get("idade", -1))
        if 0 <= idade <= 3:
            return "Faixa Etária: Berçário."
        elif 4 <= idade <= 5:
            return "Faixa Etária: Pré-escola."
        elif 6 <= idade <= 10:
            return "Faixa Etária: Ensino Fundamental I."
        else:
            return "Fora da faixa etária coberta (0-10 anos)."
    except ValueError:
        return "Erro: Por favor, digite uma idade válida."