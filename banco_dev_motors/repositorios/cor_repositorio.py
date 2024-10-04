from typing import List
from banco_dados import conectar
from entidades import Marca, Modelo, Cor


def obter_todas_cores() -> List[Cor]:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT 
        cores.id,
        cores.nome,
        cores.id_modelos,
        modelos.nome,
        marca.nome
    FROM modelos
    INNER JOIN marcas ON (cores.id_modelos = modelos.id)""")
    registros = cursor.fetchall()
    conexao.close()

    lista_cores: List[Cor] = []
    for registro in registros:
        id = registro[0]
        nome = registro[1]
        id_modelo = registro[2]
        nome_modelo = registro[3]
        id_marca = registro[4]
        nome_marca = registro[5]
        cnpj_marca = registro[6]
        marca = Marca(id_marca, nome_marca, cnpj_marca)
        modelo = Modelo(id, marca, nome)
        lista_cores.append(Cor)
    return lista_cores


def cadastrar(id_modelos: int, nome: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO cores (id_modelos, nome) VALUES (%s, %s)", (id_modelos, nome))
    conexao.commit()
    conexao.close()


def atualizar(id: int, id_modelos: int, nome: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE cores SET id_modelos = %s, nome = %s WHERE id = %s", (id_modelos, nome, id))
    conexao.commit()
    conexao.close()


def apagar(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM cores WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()


