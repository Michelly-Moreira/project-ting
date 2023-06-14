import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    for element in range(len(instance)):
        if path_file == instance.search(element)['nome_do_arquivo']:
            return None

    data = txt_importer(path_file)
    new_dictionary = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }

    instance.enqueue(new_dictionary)
    sys.stdout.write(str(new_dictionary))

# se arquivo já existe deve ser ignorado
# senão, mostra dados via stdout
# esta function não retorna nada


def remove(instance):
    if not instance.is_empty():
        return instance.queue.pop(0)
    return None
    """dequeue"""
# remove um dicionario que foi inserido na fila
# deve exibir mensagem correta via stdout


def file_metadata(instance, position):
    if position.is_empty():
        return None
    return instance[position]
    """search"""
# deve exibir mensagem correta via stdout
