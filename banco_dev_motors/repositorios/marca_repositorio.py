from typing import List
from entidades import Marca
from banco_dados import conectar


def obter_todas_marcas() -> List[Marca]:
    conexao = conectar()
    print("Conectado com Sucesso")
    # criado cursor que nos permitira executar comandos de SQL
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, cnpj FROM marcas")
    # fetchall buscar todos os registros encontrados na consulta
    registros = cursor.fetchall()
    # fechar a conexão com o banco de dados
    conexao.close() 

    marcas: List[Marca] = []
    #percorrer cada um dos registros que consultamos do banco de dados
    for registro in registros:
        #obter os valores das colunas do select
        id = registro[0]
        nome = registro[1]
        cnpj = registro[2]
        # intanciando um objeto da marca, passando como parametro no construtor
        marca = Marca(id, nome, cnpj)
        # adicionando a marca na lista de marcas 
        marcas.append(marca)
    #retornar lista de marcas
    return marcas


def cadastrar(nome: str, cnpj: str):
    conexao = conectar()

    cursor = conexao.cursor()
    cursor.execute("INSERT INTO marcas (nome, cnpj) VALUES (%s,%s)", (nome, cnpj))
    conexao.commit() # Efetuar a transação
    conexao.close() # Fechar a conexão com o bando de dados


def atualizar(id: int, nome: str, cnpj: str):
    conexao = conectar()

    cursor = conexao.cursor()
    cursor.execute("UPDATE marcas SET nome = %s, cnpj = %s WHERE id = %s", (nome, cnpj, id))
    conexao.commit()
    conexao.close()


def apagar(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM marcas WHERE id = %s" (id))
    conexao.commit() #efetuar a transação
    conexao.close()