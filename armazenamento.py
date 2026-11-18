
import json


def salvar_arquivo(caminho, materias, tarefas, sessoes):
    dados = {
        "materias": materias,
        "tarefas": tarefas,
        "sessoes": sessoes
    }

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def carregar_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
