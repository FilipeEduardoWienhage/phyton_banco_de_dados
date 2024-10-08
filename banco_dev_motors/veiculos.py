import questionary

from rich.console import Console
from rich.table import Table



def menu_veiculos():
    opcoes = [
        "Consultar",
        "Cadastrar",
        "Editar",
        "Apagar",
        "Sair"
    ]
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select("Menu Veiculos", opcoes).ask()
        if opcao_escolhida == "Consultar":
            consultar_veiculos()
        elif opcao_escolhida == "Cadastrar":
            inserir_veiculos()
        elif opcao_escolhida == "Editar":
            editar_veiculos()
        elif opcao_escolhida == "Apagar":
            apagar_veiculos()


def consultar_veiculos():
    pass


def inserir_veiculos():
    pass


def editar_veiculos():
    pass


def apagar_veiculos():
    pass