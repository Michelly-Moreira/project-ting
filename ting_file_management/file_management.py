import sys

def txt_importer(path_file):
    with open (path_file, "r") as file:
        content = file.read()
        print (content)


    # Caso o arquivo TXT não exista aparece a msg Arquivo {path_file} não encontrado na stderr, onde path_file é o caminho do arquivo
    # caso a extensão do arquivo seja diferente de .txt Formato inválido na stderr
    # A função deve retornar uma lista contendo as linhas do arquivo
