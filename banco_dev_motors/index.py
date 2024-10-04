from marcas import menu_marcas
from modelos import menu_modelos
from banco_dev_motors.cores import menu_cores
import questionary

def menu():
    opcoes = [
        "Marcas",
        "Modelos",
        "Cores",
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
        elif menu_escolhido == "Cores":
            menu_cores()

if __name__ == "__main__":
    menu()