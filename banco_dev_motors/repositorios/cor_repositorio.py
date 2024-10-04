from typing import List
from banco_dados import conectar
from entidades import Cor


def obter_todas_cores() -> List[Cor]:
     conexao = conectar()
     cursor = conexao.cursor()
     cursor.execute("""
     SELECT 
         cores.id,
         cores.nome
     FROM cores
     """)
     registros = cursor.fetchall()
     conexao.close()

     lista_cores: List[Cor] = []
     for registro in registros:
         id = registro[0]
         nome = registro[1]
         cor = Cor(id, nome)
         lista_cores.append(cor)
     return lista_cores


def cadastrar_cores(nome: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO cores (nome) VALUES (%s)", (nome,))
    conexao.commit()
    conexao.close()


def atualizar_cores(id: int, nome: str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE cores SET  nome = %s WHERE id = %s", (nome, id))
    conexao.commit()
    conexao.close()


def apagar_cores(id: int):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM cores WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()


