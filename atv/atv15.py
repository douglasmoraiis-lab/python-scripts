def run(form):
    try:
        l1 = float(form.get("lado1", 0))
        l2 = float(form.get("lado2", 0))
        l3 = float(form.get("lado3", 0))

        if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
            if l1 == l2 == l3:
                return "Os lados formam um triângulo EQUILÁTERO."
            elif l1 == l2 or l1 == l3 or l2 == l3:
                return "Os lados formam um triângulo ISÓSCELES."
            else:
                return "Os lados formam um triângulo ESCALENO."
        else:
            return "Os lados informados NÃO formam um triângulo."
    except ValueError:
        return "Erro: Por favor, digite valores numéricos válidos para os lados."