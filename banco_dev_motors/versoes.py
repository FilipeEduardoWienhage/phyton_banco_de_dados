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
    versoes = obter_todas_versoes()
    if len(versoes) == 0:
        print("Nenhuma versão cadastrada")
        return
    
    opcoes_para_escolher = []
    for versao in versoes:
        opcoes_para_escolher.append(questionary.Choice(versao.nome, versao.id))

    id_versao_escolhida = questionary.select(
        "Escolha a versão para alterar", opcoes_para_escolher,
    ).ask()
    
    modelos = obter_todos_modelos()
    if len(modelos) == 0:
        print("Nenhum modelo cadastrado")
        return
    
    opcoes_modelos_para_escolher = []
    for modelo in modelos:
        opcoes_modelos_para_escolher.append(questionary.Choice(modelo.nome, modelo.id))
    
    nome = questionary.text("Digite o nome da versão: ").ask()
    motor = questionary.text("Digite a motorização da versão: ").ask()
    id_modelo = questionary.select("Escolha o modelo", opcoes_modelos_para_escolher).ask()
    atualizar(id_versao_escolhida, id_modelo, nome, motor)
    

def apagar_versao():
    versoes = obter_todas_versoes()
    if len(versoes) == 0:
        print("Nenhuma versão cadastrada")
        return  
    
    opcoes_para_escolher = []
    for versao in versoes:
        opcao = questionary.Choice(versao.nome, versao.id)
        opcoes_para_escolher.append(opcao)
    id_versao_escolhida = questionary.select(
        "Escolha a versão para apagar", opcoes_para_escolher,
    ).ask()
    apagar(id_versao_escolhida)


def consultar_versao():
    versoes = obter_todas_versoes()
    if len(versoes) == 0:
        print("Nenhuma versão cadastrada")
        return

    tabela = Table(title="Lista de Versões")
    tabela.add_column("Código")
    tabela.add_column("Marca")
    tabela.add_column("Modelo")
    tabela.add_column("Motorização")
    tabela.add_column("Versão")

    for versao in versoes:
        tabela.add_row(
            str(versao.id), 
            versao.modelo.marca.nome, 
            versao.modelo.nome, 
            versao.nome, 
            versao.motor
        )
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

