import questionary
from repositorios.venda_repositorio import obter_todas_vendas, cadastrar, atualizar, apagar
from rich.console import Console
from rich.table import Table



def menu_venda():
    opcoes = [
        "Consultar",
        "Cadastrar",
        "Editar",
        "Apagar",
        "Sair"
    ]
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select("Menu Venda", opcoes).ask()
        if opcao_escolhida == "Consultar":
            consultar_vendas()
        elif opcao_escolhida == "Cadastrar":
            inserir_vendas()
        elif opcao_escolhida == "Editar":
            editar_vendas()
        elif opcao_escolhida == "Apagar":
            apagar_vendas()


def consultar_vendas():
    pass


def inserir_vendas():
    pass


def editar_vendas():
    pass


def apagar_vendas():
    pass