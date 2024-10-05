from typing import List
from banco_dados import conectar
from entidades import Modelo, Versao


def cadastrar(id_modelo: int, nome: str, motor: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO versoes (id_modelo, nome, motor) VALUES (%s, %s, %s)", (id_modelo, nome, motor))
    conexao.commit()
    conexao.close()


def atualizar():
    pass


def obter_todas_versoes() -> List[Versao]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT versoes.id, versoes.nome, versoes.motor, modelos.id, modelos.nome 
        FROM versoes 
        INNER JOIN modelos ON versoes.id_modelo = modelos.id""")
    registros = cursor.fetchall()
    conexao.close()

    lista_versoes: List[Versao] = []
    for registro in registros:
        id = registro[0]
        nome = registro[1]
        motor = registro[2]
        id_modelo = registro[3]
        nome_modelo = registro[4]
        modelo = Modelo(id_modelo, nome_modelo)
        versao = Versao(id, modelo, nome, motor)
        lista_versoes.append(versao)
    return lista_versoes


def apagar():
    pass
