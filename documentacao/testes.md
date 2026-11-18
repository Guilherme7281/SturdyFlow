
# Relatório de Testes — SturdyFlow

## 1. Identificação

- **Projeto:** SturdyFlow — Organizador de Estudos
- **Etapa:** Aula 04
- **Tipo de teste:** Unitário, integração e sistema
- **Ambiente:** Windows 11, Python 3.14.8
- **Interface:** Tkinter

## 2. Testes unitários

Foram executados seis testes automatizados utilizando a biblioteca unittest.

| ID | Caso de teste | Resultado esperado | Resultado |
|---|---|---|---|
| UT01 | Validar data correta | Retornar verdadeiro | Aprovado |
| UT02 | Validar data inexistente | Retornar falso | Aprovado |
| UT03 | Validar duração positiva | Retornar verdadeiro | Aprovado |
| UT04 | Validar duração zero | Retornar falso | Aprovado |
| UT05 | Verificar campos preenchidos | Retornar verdadeiro | Aprovado |
| UT06 | Verificar campo vazio | Retornar falso | Aprovado |

**Resultado:** 6 testes aprovados.

## 3. Testes de integração

Foram executados dois testes automatizados para verificar a comunicação entre as funções de gravação e leitura de arquivos JSON.

| ID | Caso de teste | Resultado esperado | Resultado |
|---|---|---|---|
| IT01 | Salvar e carregar matérias, tarefas e sessões | Recuperar os dados sem alterações | Aprovado |
| IT02 | Salvar e carregar listas vazias | Recuperar as listas vazias corretamente | Aprovado |

**Resultado:** 2 testes aprovados.

Os testes utilizaram arquivos temporários, sem modificar os dados reais do programa.

## 4. Testes de sistema

Foram realizados testes manuais diretamente na interface do SturdyFlow.

| ID | Caso de teste | Resultado esperado | Resultado |
|---|---|---|---|
| ST01 | Navegar entre as telas | Abrir todas as seções normalmente | Aprovado |
| ST02 | Cadastrar matéria | Exibir a matéria na lista | Aprovado |
| ST03 | Manter matéria após reiniciar | Preservar os dados | Aprovado |
| ST04 | Cadastrar tarefa | Exibir os dados da tarefa | Aprovado |
| ST05 | Concluir tarefa | Alterar o status para concluída | Aprovado |
| ST06 | Manter conclusão após reiniciar | Preservar o status | Aprovado |
| ST07 | Registrar sessão de estudo | Cadastrar e exibir a sessão | Aprovado |
| ST08 | Inserir data inexistente | Impedir o cadastro | Aprovado |
| ST09 | Inserir duração igual a zero | Impedir o cadastro | Aprovado |
| ST10 | Remover matéria vinculada | Impedir a remoção | Aprovado |
| ST11 | Cadastrar matéria sem nome | Impedir o cadastro | Aprovado |

## 5. Resultado geral

- Testes unitários: 6 aprovados.
- Testes de integração: 2 aprovados.
- Testes de sistema: 11 aprovados.

Não foram identificadas falhas durante os testes realizados.

## 6. Conclusão

Os testes realizados demonstraram que as funcionalidades verificadas do SturdyFlow apresentaram o comportamento esperado.

As validações de dados, o armazenamento em JSON, o cadastro de informações e a navegação entre as telas foram verificados com resultados satisfatórios.

A execução dos testes contribuiu para avaliar a confiabilidade do sistema e identificar possíveis problemas antes da entrega do projeto.
