
import unittest
import tempfile
import os

from regras import validar_data, validar_duracao, campos_preenchidos
from armazenamento import salvar_arquivo, carregar_arquivo


class TestRegras(unittest.TestCase):

    def test_data_valida(self):
        self.assertTrue(validar_data("18/11/2026"))

    def test_data_invalida(self):
        self.assertFalse(validar_data("31/02/2026"))

    def test_duracao_valida(self):
        self.assertTrue(validar_duracao("60"))

    def test_duracao_invalida(self):
        self.assertFalse(validar_duracao("0"))

    def test_campos_preenchidos(self):
        self.assertTrue(campos_preenchidos("Matemática", "18/11/2026"))

    def test_campos_vazios(self):
        self.assertFalse(campos_preenchidos("Matemática", ""))


class TestArmazenamento(unittest.TestCase):

    def test_salvar_e_carregar_dados(self):
        materias = ["Matemática", "Programação"]

        tarefas = [
            {
                "nome": "Estudar Python",
                "materia": "Programação",
                "data": "20/11/2026",
                "concluida": False
            }
        ]

        sessoes = [
            {
                "materia": "Matemática",
                "data": "18/11/2026",
                "duracao": 60
            }
        ]

        with tempfile.TemporaryDirectory() as pasta:
            caminho = os.path.join(pasta, "teste.json")

            salvar_arquivo(caminho, materias, tarefas, sessoes)
            dados = carregar_arquivo(caminho)

            self.assertEqual(dados["materias"], materias)
            self.assertEqual(dados["tarefas"], tarefas)
            self.assertEqual(dados["sessoes"], sessoes)

    def test_salvar_dados_vazios(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = os.path.join(pasta, "teste.json")

            salvar_arquivo(caminho, [], [], [])
            dados = carregar_arquivo(caminho)

            self.assertEqual(dados["materias"], [])
            self.assertEqual(dados["tarefas"], [])
            self.assertEqual(dados["sessoes"], [])


if __name__ == "__main__":
    unittest.main()