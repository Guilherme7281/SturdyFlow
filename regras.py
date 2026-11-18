
from datetime import datetime


def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def validar_duracao(duracao):
    try:
        minutos = int(duracao)
        return minutos > 0
    except ValueError:
        return False


def campos_preenchidos(*campos):
    return all(campo.strip() for campo in campos)
