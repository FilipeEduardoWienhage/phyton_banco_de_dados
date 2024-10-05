from typing import List
from banco_dados import conectar
from entidades import Opcional


def obter_todos_opcionais() -> List[Opcional]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome FROM opcionais")
    registros = cursor.fetchall()
    conexao.close()

    opcionais: List[Opcional] = []
    for registro in registros:
        id = registro[0]
        nome = registro[1]

        opcional = Opcional(id,nome)
        opcionais.append(opcional)
    return(opcionais)


def cadastrar(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO opcionais (nome) VALUES (%s)", (nome,))
    conexao.commit()
    conexao.close()

def atualizar(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE opcionais SET nome = %s", (nome,))
    conexao.commit()
    conexao.close()


def apagar(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM opcionais WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()