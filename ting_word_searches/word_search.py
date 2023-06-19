def exists_word(word, instance):
    result = []
    counter = 0

    for element in range(len(instance)):
        file_actual = instance.search(element)
        frame = {
            "palavra": word,
            "arquivo": file_actual["nome_do_arquivo"],
            "ocorrencias": [{
                "linha": index + 1
            } for index, linha in enumerate(file_actual["linhas_do_arquivo"])
                if word.lower() in linha.lower()]
        }
        result.append(frame)
        if len(frame["ocorrencias"]) == 0:
            counter += 1

    if counter == len(instance):
        return []
    return result


def search_by_word(word, instance):
    result= []
    counter = 0

    for element in range(len(instance)):
        file_actual = instance.search(element)
        frame = {
            "palavra": word,
            "arquivo": file_actual["nome_do_arquivo"],
            "ocorrencias": [{
                "linha": index + 1,
                "conteudo": linha
            } for index, linha in enumerate(file_actual["linhas_do_arquivo"])
                if word.lower() in linha.lower()]
        }
        result.append(frame)
        if len(frame["ocorrencias"]) == 0:
            counter += 1

    if counter == len(instance):
        return []
    return result