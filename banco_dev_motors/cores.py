import questionary
from repositorios.cor_repositorio import cadastrar_cores, atualizar_cores, apagar_cores, obter_todas_cores
from rich.console import Console
from rich.table import Table
import os


def limpar_tela():
    os.system("cls")

def menu_cores():
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select(
        "Menu de Cores",
        choices=[
            "Consultar cores",
            "Cadastrar cores",
            "Editar cores",
            "Apagar cores",
            "Sair"
        ]).ask()
        limpar_tela()

        if opcao_escolhida == "Consultar cores":
            consultar_cores()
        elif opcao_escolhida == "Cadastrar cores":
            inserir_cores()
        elif opcao_escolhida == "Editar cores":
            editar_cores()
        elif opcao_escolhida == "Apagar cores":
            apagar_cor()


def consultar_cores():
    cores = obter_todas_cores()
    if len(cores) == 0:
        print("Nenhuma cor cadastrada")
        return
    
    table = Table(title="Consulta de Cores")

    table.add_column("Código", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nome", justify="center", style="magenta")

    for cor in cores:
        table.add_row(str(cor.id), cor.nome)

    console = Console()
    console.print(table)


def inserir_cores():
    
    nome = questionary.text("Informe o nome da cor: ").ask()
    cadastrar_cores(nome)
    print("Cor cadastrada com sucesso")


def apagar_cor():
    cores = obter_todas_cores()
    if len(cores) == 0:
        print("Nenhuma cor cadastrado")
        return
    
    opcoes_para_escolher = []
    for cor in cores:
        opcao = questionary.Choice(cor.nome, cor.id)
        opcoes_para_escolher.append(opcao)
    # Perguntar para o usuário qual a cor que deseja apagar,
    # quando usuário escolher a cor será armazenado o id
    id_cor_escolhida = questionary.select(
        "Escolha a cor para apagar",
        choices=opcoes_para_escolher,
    ).ask()
    # Chamar função para apagar
    apagar_cores(id_cor_escolhida)


def editar_cores():
    cores = obter_todas_cores()
    if len(cores) == 0:
        print("Nenhuma cor cadastrada")
        return
    
    opcoes_para_escolher = []
    for cor in cores:
        opcao = questionary.Choice(cor.nome, cor.id)
        opcoes_para_escolher.append(opcao)
    # Perguntar para o usuário qual a cor que deseja alterar,
    # quando usuário escolher a cor será armazenado o id
    id_cor_escolhida = questionary.select(
        "Escolha a cor para alterar",choices=opcoes_para_escolher,
    ).ask()

    cor_editada = questionary.text("Informe o nome da cor: ").ask()
    atualizar_cores(id_cor_escolhida, cor_editada)
