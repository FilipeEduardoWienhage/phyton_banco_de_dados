import questionary
import os
from rich.console import Console
from rich.table import Table
from repositorios.marca_repositorio import obter_todas_marcas, cadastrar, atualizar, apagar


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
    cadastrar(nome, cnpj)
    print("Marca cadastrada com sucesso")


def consultar_marcas(): # read
    marcas = obter_todas_marcas()
    # Verificando se existe uma marca cadastrada
    if len(marcas) == 0:
        print("Nenhuma marca cadastrada")
        return

    table = Table(title="Consulta de Marcas")

    table.add_column("Código", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nome", justify="center", style="magenta")
    table.add_column("CNPJ", justify="center", style="green")

    for marca in marcas:
        table.add_row(str(marca.id), marca.nome, marca.cnpj)

    console = Console()
    console.print(table)  


def atualizar_marca(): # update
    marcas = obter_todas_marcas()
    if len(marcas) == 0:
        print("Nenhuma marca cadastrada")
        return

    opcoes_para_escolher = []
    for marca in marcas:
        opcao = questionary.Choice(title=marca.nome, value=marca.id)
        opcoes_para_escolher.append(opcao)

    id_marca_escolhida = questionary.select(
        "Escolha a marca que deseja editar",
        choices=opcoes_para_escolher
    ).ask()

    nome_editado = questionary.text("Informe o nome da marca: ").ask()
    cnpj_editado = questionary.text("Informe o CNPJ: ").ask()
    atualizar(id_marca_escolhida, nome_editado, cnpj_editado)

def apagar_marca(): # delete
    # Consultar todas as marcas
    marcas = obter_todas_marcas()
    if len(marcas) == 0:
        print("Nenhuma marca cadastrada")
        return
    # Criar um vetor com as marcas para o usuario poder escolher a marca que deseja apagar
    opcoes = []
    for marca in marcas:
        opcao = questionary.Choice(marca.nome, marca.id)
        opcoes.append(opcao)

    # Perguntando para o usuario qual marca ele deseja apagar
    id_para_apagar = questionary.select(
        "Escolha uma marca para apagar",
        choices=opcoes,
    ).ask()
    # Abrir a conexão
    apagar(id_para_apagar)

