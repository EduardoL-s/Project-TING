def exists_word(word, instance):
    result_exists_word = []

    for index in range(len(instance)):
        result = instance.search(index)
        word_search_dict = {
            "palavra": word,
            "arquivo": result["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for line_index, line in enumerate(result["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                word_search_dict["ocorrencias"].append({"linha": line_index+1})

        if len(word_search_dict["ocorrencias"]) > 0:
            result_exists_word.append(word_search_dict)
    return result_exists_word


def search_by_word(word, instance):
    result_exists_word = []

    for index in range(len(instance)):
        result = instance.search(index)
        word_search_dict = {
            "palavra": word,
            "arquivo": result["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for line_index, line in enumerate(result["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                word_search_dict["ocorrencias"].append({
                    "linha": line_index+1,
                    "conteudo": line,
                    })

        if len(word_search_dict["ocorrencias"]) > 0:
            result_exists_word.append(word_search_dict)
    return result_exists_word
