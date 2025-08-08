import os
import importlib
from flask import Flask, render_template, request, abort

app = Flask(__name__)
def encontrar_atividades():
    """Encontra todos os arquivos atvX.py na pasta 'atv' e os ordena numericamente."""
    try:
        arquivos = os.listdir('atv')
        lista_bruta = [f[:-3] for f in arquivos if f.startswith('atv') and f.endswith('.py')]
        
        # A MÁGICA ACONTECE AQUI:
        # Ordenamos a lista usando uma chave que extrai o número e o converte para inteiro.
        # Ex: 'atv5' -> 5, 'atv12' -> 12. Assim, 5 vem antes de 12.
        atividades = sorted(lista_bruta, key=lambda s: int(s.replace('atv', '')))
        
        return atividades
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    """Renderiza a página inicial com o menu de atividades."""
    atividades = encontrar_atividades()
    return render_template('index.html', activities=atividades)

@app.route('/<act>', methods=['GET', 'POST'])
def activity(act):
    """
    Rota dinâmica para cada atividade.
    GET: Mostra o formulário HTML (atvX.html).
    POST: Processa os dados do formulário com o script Python (atvX.py).
    """
    atividades = encontrar_atividades()
    if act not in atividades:
        abort(404)  # Atividade não encontrada

    try:
        # Importa dinamicamente o módulo da atividade (ex: atv.atv5)
        modulo_atividade = importlib.import_module(f'atv.{act}')
    except ImportError:
        abort(500, description=f"Não foi possível importar o módulo {act}.py")

    if request.method == 'POST':
        # Converte os dados do formulário para um dicionário padrão
        form_data = request.form.to_dict()
        
        # Verifica se a função 'run' existe no módulo
        if hasattr(modulo_atividade, 'run'):
            # Chama a função 'run' e passa os dados do formulário
            resultado = modulo_atividade.run(form_data)
        else:
            # Mensagem de erro clara se a função não for encontrada
            resultado = f"ERRO: A função 'run(form)' não foi encontrada no arquivo {act}.py."
        
        return render_template('result.html', act=act, result=resultado)
    
    # Se o método for GET, apenas mostra o formulário da atividade
    return render_template(f'{act}.html', act=act)

if __name__ == '__main__':
    # Cria o arquivo __init__.py se não existir
    if not os.path.exists('atv/__init__.py'):
        with open('atv/__init__.py', 'w') as f:
            pass
            
    app.run(debug=True)