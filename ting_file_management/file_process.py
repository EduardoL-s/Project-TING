from ting_file_management.file_management import txt_importer
import sys

def process(path_file, instance):
    news = txt_importer(path_file)
    news_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(news),
        "linhas_do_arquivo": news,
    }

    for index in range(len(instance)):
        queue_content = instance.search(index)
        if queue_content == news_dict:
            return

    instance.enqueue(news_dict)
    print(news_dict, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print('Não há elementos', file=sys.stdout)
        return
    
    removed_content = instance.dequeue()
    removed_content_path = removed_content["nome_do_arquivo"]
    print(f"Arquivo {removed_content_path} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        print(result, file=sys.stdout)
    except IndexError: print('Posição inválida', file=sys.stderr)

