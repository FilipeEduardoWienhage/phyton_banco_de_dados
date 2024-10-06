from typing import List
from banco_dados import conectar
from entidades import Modelo, Versao, Marca


def cadastrar(id_modelo: int, nome: str, motor: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO versoes (id_modelo, nome, motor) VALUES (%s, %s, %s)", (id_modelo, nome, motor))
    conexao.commit()
    conexao.close()


def atualizar(id: int, id_modelo: int, nome: str, motor: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE versoes SET id_modelo = %s, nome = %s, motor = %s WHERE id = %s",
        (id_modelo, nome, motor, id))
    conexao.commit()
    conexao.close()


def obter_todas_versoes() -> List[Versao]:
    conexao = conectar()
    cursor = conexao.cursor()
    # Query que traz as versões, modelos e marcas associadas
    cursor.execute("""
        SELECT 
            versoes.id, 
            versoes.nome AS nome_versao, 
            versoes.motor, 
            modelos.id AS modelo_id, 
            modelos.nome AS nome_modelo, 
            marcas.id AS marca_id, 
            marcas.nome AS nome_marca, 
            marcas.cnpj AS cnpj_marca
        FROM versoes
        INNER JOIN modelos ON versoes.id_modelo = modelos.id
        INNER JOIN marcas ON modelos.id_marca = marcas.id
    """)
    registros = cursor.fetchall()
    conexao.close()
    lista_versoes: List[Versao] = []
    # Processar cada registro retornado pela query
    for registro in registros:
        id_versao = registro[0]
        nome_versao = registro[1]
        motor = registro[2]
        id_modelo = registro[3]
        nome_modelo = registro[4]
        id_marca = registro[5]
        nome_marca = registro[6]
        cnpj_marca = registro[7]
        # Criar os objetos Marca, Modelo e Versão
        marca = Marca(id_marca, nome_marca, cnpj_marca)
        modelo = Modelo(id_modelo, marca, nome_modelo)
        versao = Versao(id_versao, modelo, motor, nome_versao)
        lista_versoes.append(versao)
    return lista_versoes


def apagar(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM versoes WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()