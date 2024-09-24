import mysql.connector
import questionary
import os
from rich.console import Console
from rich.table import Table

# CRUD
# Create
# Read
# Update
# Delete


def limpar_tela():
    os.system("cls")


def menu_marcas():
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select(
        "Menu de Marcas",
        choices=[
            "Consultar marcas",
            "Cadastrar marca",
            "Editar marca",
            "Apagar marca",
            "Sair"
        ]).ask()
        limpar_tela()

        if opcao_escolhida == "Consultar marcas":
            consultar_marcas()
        elif opcao_escolhida == "Cadastrar marca":
            inserir_marca()
        elif opcao_escolhida == "Editar marca":
            atualizar_marca()
        elif opcao_escolhida == "Apagar marca":
            apagar_marca()

def inserir_marca(): # create

    nome = questionary.text("Informe o nome da marca: ").ask()
    cnpj = questionary.text("Informe o CNPJ: ").ask()
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="a1s2d3f4" 
    )
    print("Conectado com Sucesso")
    cursor = conexao.cursor()
    cursor.execute("use dev_motors")
    cursor.execute(f"INSERT INTO marcas (nome, cnpj) VALUES ('{nome}', '{cnpj}');")
    conexao.commit() # Efetuar a transação
    conexao.close() # Fechar a conexão com o bando de dados
    print("Marca cadastrada com sucesso")


def consultar_marcas(): # read
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="a1s2d3f4",
        database="dev_motors" 
    )
    print("Conectado com Sucesso")
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, cnpj FROM marcas")
    # fetchall buscar todos os registros encontrados na consulta
    registros = cursor.fetchall()
    # fechar a conexão com o banco de dados
    conexao.close() 

    table = Table(title="Consulta de Marcas")

    table.add_column("Código", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nome", justify="center", style="magenta")
    table.add_column("CNPJ", justify="center", style="green")

    for registro in registros:
        codigo = registro[0]
        nome = registro[1]
        cnpj = registro[2]
        table.add_row(str(codigo), nome, cnpj)

    console = Console()
    console.print(table)  


def atualizar_marca(): # update
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="a1s2d3f4",
        database="dev_motors" 
    )
    print("Conectado com Sucesso")
    cursor = conexao.cursor()
    cursor.execute("UP")


def apagar_marca(): # delete
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="a1s2d3f4",
        database="dev_motors" 
    )
    print("Conectado com Sucesso")
    cursor = conexao.cursor()
    cursor.execute("DELETE * FROM marcas")
    conexao.commit() 
    conexao.close()

if __name__ == "__main__":
    menu_marcas()