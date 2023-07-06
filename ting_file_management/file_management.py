import sys


def txt_importer(path_file):
    if '.txt' not in path_file:
        print('Formato inválido', file=sys.stderr)
        # método de exibir mensagem no stderr disponível em:
        # https://stackoverflow.com/questions/5574702/how-do-i-print-to-stderr-in-python
        return

    try:
        with open(path_file, 'r') as text:
            lines = text.read().split('\n')
            # método para acessar e ler arquivo .txt disponível em:
            # https://www.hashtagtreinamentos.com/trabalhar-com-arquivos-de-texto-python?gad=1&gclid=CjwKCAjwzJmlBhBBEiwAEJyLu8uGvX9jDYLLwQvmVn6nz--MtluIvHMwg1jBq8l7HYWF8hUba2EWZxoCR90QAvD_BwE
            return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
