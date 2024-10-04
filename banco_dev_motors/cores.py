import questionary
from repositorios.marca_repositorio import obter_todas_marcas
from repositorios.modelo_repositorio import apagar, atualizar, cadastrar, obter_todos_modelos
from repositorios.cor_repositorio import obter_todas_cores, cadastrar, atualizar, apagar
from rich.console import Console
from rich.table import Table


def menu_cores():
    opcoes = [
        "Consultar",
        "Cadastrar",
        "Editar",
        "Apagar",
        "Sair"
    ]
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select("Menu de Cores", opcoes).ask()
        if opcao_escolhida == "Consultar":
            consultar_cores()
        elif opcao_escolhida == "Cadastrar":
            inserir_cores()
        elif opcao_escolhida == "Apagar":
            apagar_cores()
        elif opcao_escolhida == "Editar":
            editar_cores()


def consultar_cores():
    # Buscar no banco de dados os modelos para listarmos para o usuário
    cores = obter_todas_cores()
    if len(cores) == 0:
        print("Nenhuma cor cadastrada")
        return

    # Criar a tabela (que apresentaremos os registros) com seu cabeçalho
    tabela = Table(title="Lista de Cores")
    tabela.add_column("Código")
    tabela.add_column("Cor")

    for cor in cores:
        tabela.add_row(str(cor.id), cor.id, cor.nome)

    console = Console()
    console.print(tabela)


def inserir_cores():
    cores = obter_todas_cores()
    if len(cores) == 0:
        print("Nenhuma cor cadastrada")
        return
    
    opcoes_cores_para_escolher = []
    for cor in cores:
        opcao = questionary.Choice(cor.nome, cor.id)
        opcoes_cores_para_escolher.append(opcao)
    
    id_cor_escolhida = questionary.select("Escolha a cor", opcoes_cores_para_escolher).ask()

    nome = questionary.text("Digite o nome da Cor").ask()
    cadastrar(id_cor_escolhida, nome)
    print("Cadastrado com sucesso")


def apagar_cores():
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
        "Escolha a cor para apagar", opcoes_para_escolher,
    ).ask()
    # Chamar função para apagar
    apagar(id_cor_escolhida)


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
    id_modelo_escolhido = questionary.select(
        "Escolha a cor para alterar", opcoes_para_escolher,
    ).ask()
    marcas = obter_todas_marcas()
    if len(marcas) == 0:
        print("Nenhuma marca cadastrada")
        return
    
    opcoes_marcas_para_escolher = []
    for modelo in modelos:
        opcao = questionary.Choice(modelo.nome, modelo.id)
        opcoes_marcas_para_escolher.append(opcao)
    
    # Perguntar o nome da nova cor
    nome = questionary.text("Digite o nome da cor").ask()
    id_marca = questionary.select("Escolha a marca", opcoes_marcas_para_escolher).ask()
    # Atualizar o registro na tabela de modelos 
    atualizar(id_modelo_escolhido, id_marca, nome)
