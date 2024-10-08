import questionary
import os
from rich.console import Console
from rich.table import Table
from repositorios.veiculo_opcional_repositorio import obter_todos_veiculos_opcionais, apagar, atualizar, cadastrar


def limpar_tela():
    os.system("cls")


def menu_veiculos_opcionais():
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select(
        "Menu de Veiculos",
        choices=[
            "Consultar veiculos opcionais",
            "Cadastrar veiculos opcionais",
            "Editar veiculos opcionais",
            "Apagar veiculos opcionais",
            "Sair"
        ]).ask()
        limpar_tela()

        if opcao_escolhida == "Consultar veiculos opcionais":
            consultar_veiculos_opcionais()
        elif opcao_escolhida == "Cadastrar veiculos opcionais":
            inserir_veiculos_opcional()
        elif opcao_escolhida == "Editar veiculos opcionais":
            atualizar_veiculos_opcionais()
        elif opcao_escolhida == "Apagar veiculos opcionais":
            apagar_veiculos_opcionais()


def inserir_veiculos_opcional():
    pass


def consultar_veiculos_opcionais():
    pass


def atualizar_veiculos_opcionais():
    pass


def apagar_veiculos_opcionais():
    pass