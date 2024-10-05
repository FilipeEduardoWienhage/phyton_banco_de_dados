import questionary
import os
from rich.console import Console
from rich.table import Table
from repositorios.opcional_repositorio import cadastrar, apagar, obter_todos_opcionais, atualizar


def limpar_tela():
    os.system("cls")


def menu_opcionais():
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select(
        "Menu de Opcionais",
        choices=[
            "Consultar opcionais",
            "Cadastrar opcionais",
            "Editar opcionais",
            "Apagar opcionais",
            "Sair"
        ]).ask()
        limpar_tela()

        if opcao_escolhida == "Consultar opcionais":
            consultar_opcionais()
        elif opcao_escolhida == "Cadastrar opcionais":
            inserir_opcionais()
        elif opcao_escolhida == "Editar opcionais":
            atualizar_opcionais()
        elif opcao_escolhida == "Apagar opcionais":
            apagar_opcionais()            
            

def consultar_opcionais():
    opcionais = obter_todos_opcionais()
    if len(opcionais) == 0:
        print("Nenhum Opcional Cadastrado")
        return
    
    table = Table(title="Consulta de Opcionais")

    table.add_column("Código", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nome", justify="center", style="magenta")
    
    for opcional in opcionais:
        table.add_row(str(opcional.id), opcional.nome)

    console = Console()
    console.print(table)

def inserir_opcionais():
    nome = questionary.text("Informe o nome do opcional").ask()
    cadastrar(nome)
    print("Opcional cadastrado com sucesso")


def atualizar_opcionais():
    opcionais = obter_todos_opcionais()
    if len(opcionais) == 0:
        print("Nenhum opcional cadastrado")
        return
    
    opcoes_para_escolher = []
    for opcional in opcionais:
        opcao = questionary.Choice(opcional.nome)
        opcoes_para_escolher.append(opcao)

    id_opcao_escolhida = questionary.select(
        "Escolha o opcional para editar",
        choices=opcoes_para_escolher
    ).ask()

    nome_editado = questionary.text("Informe o nome: ").ask()
    atualizar(nome_editado)

def apagar_opcionais():
    opcionais = obter_todos_opcionais()
    if len(opcionais) == 0:
        print("Nenhum Opcional cadastrado")
        return

    opcoes = []
    for opcional in opcionais:
        opcao = questionary.Choice(opcional.nome, opcional.id)
        opcoes.append(opcao)

    id_apagar_opcional = questionary.select(
        "Escolha um Opcional para apagar",
        choices=opcoes,
    ).ask()
    apagar(id_apagar_opcional)
