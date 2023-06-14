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
    if len(instance) != 0:
        clear = instance.dequeue()
        print(f"Arquivo {clear['nome_do_arquivo']} removido com sucesso",
              file=sys.stdout)
    else:
        print("Não há elementos", file=sys.stdout)
        return None

# remove um dicionario da fila
# deve exibir mensagem correta via stdout


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except Exception:
        print('Posição inválida', file=sys.stderr)

# busca o dicionario pelo índice e retorna
# ou exibe mensagem de exceção via stdout
