from marcas import menu_marcas
from modelos import menu_modelos
from cores import menu_cores
from proprietarios import menu_proprietarios
from opcionais import menu_opcionais
from clientes import menu_clientes
from versoes import menu_versoes
from veiculos import menu_veiculos
from venda import menu_venda
from veiculos_opcionais import menu_veiculos_opcionais
import questionary

def menu():
    opcoes = [
        "Marcas",
        "Modelos",
        "Versões",
        "Veiculos",
        "Cores",
        "Proprietarios",
        "Opcionais",
        "Clientes",
        "Vendas",
        "Veiculos Opcionais",
        "Sair"
    ]
    menu_escolhido = ""
    while menu_escolhido != "Sair":
        menu_escolhido = questionary.select(
            "Escolha o menu desejado", opcoes
        ).ask()
        if menu_escolhido == "Marcas":
            menu_marcas()
        elif menu_escolhido == "Modelos":
            menu_modelos()
        elif menu_escolhido == "Versões":
            menu_versoes()
        elif menu_escolhido == "Veiculos":
            menu_veiculos()
        elif menu_escolhido == "Cores":
            menu_cores()
        elif menu_escolhido == "Proprietarios":
            menu_proprietarios()
        elif menu_escolhido == "Opcionais":
            menu_opcionais()
        elif menu_escolhido == "Clientes":
            menu_clientes()
        elif menu_escolhido == "Vendas":
            menu_venda()
        elif menu_escolhido == "Veiculos Opcionais":
            menu_veiculos_opcionais()


if __name__ == "__main__":
    menu()