from marcas import menu_marcas
from modelos import menu_modelos
import questionary

def menu():
    opcoes = [
        "Marcas",
        "Modelos",
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


if __name__ == "__main__":
    menu()