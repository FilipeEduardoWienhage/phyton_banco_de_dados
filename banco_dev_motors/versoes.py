import questionary
from repositorios.modelo_repositorio import obter_todos_modelos
from repositorios.versao_repositorio import apagar, atualizar, cadastrar, obter_todas_versoes
from rich.console import Console
from rich.table import Table


def menu_versoes():
    opcoes = [
        "Consultar",
        "Cadastrar",
        "Editar",
        "Apagar",
        "Sair"
    ]
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select("Menu Versões", opcoes).ask()
        if opcao_escolhida == "Consultar":
            consultar_versao()
        elif opcao_escolhida == "Cadastrar":
            inserir_versao()
        elif opcao_escolhida == "Editar":
            editar_versao()
        elif opcao_escolhida == "Apagar":
            apagar_versao()


def editar_versao():
    pass

def apagar_versao():
    pass


def consultar_versao():
    versoes = obter_todas_versoes()
    if len(versoes) == 0:
        print("Nenhuma versão cadastrada")
        return
    
    tabela = Table(title="Lista de Versões")
    tabela.add_column("Código")
    tabela.add_column("Modelo")
    tabela.add_column("Versão")
    tabela.add_column("Motorização")

    for versao in versoes:
        tabela.add_row(str(versao.id), versao.modelo.nome, versao.nome, versao.motor)

    console = Console()
    console.print(tabela)

def inserir_versao():
    modelos = obter_todos_modelos()
    if len(modelos) == 0:
        print("Nenhum Modelo Cadastrado")
        return
    
    opcoes_modelos_para_escolher = []
    for modelo in modelos:
        opcao = questionary.Choice(modelo.nome, modelo.id)
        opcoes_modelos_para_escolher.append(opcao)

    id_modelo_escolhido = questionary.select("Escolha o Modelo", opcoes_modelos_para_escolher).ask()

    nome = questionary.text("Digite o nome da versão").ask()
    motor = questionary.text("Digite a motorização da versão").ask()
    cadastrar(id_modelo_escolhido, nome, motor)
    print("Cadastrado com sucesso")

