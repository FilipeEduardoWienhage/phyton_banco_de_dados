import questionary
from repositorios.modelo_repositorio import cadastrar
from repositorios.marca_repositorio import obter_todas_marcas

def menu_modelos():
    opcoes = [
        "Consultar",
        "Cadastrar",
        "Editar",
        "Apagar",
        "Sair"
    ]
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select("Menu de Modelos", opcoes).ask()
        if opcao_escolhida == "Consultar":
            pass
        elif opcao_escolhida == "Cadastrar":
            inserir_modelo()


def inserir_modelo():
    marcas = obter_todas_marcas()
    if len(marcas) == 0:
        print("Nenhuma marca cadastrada")
        return
    
    opcoes_marcas_para_escolher = []
    for marca in marcas:
        opcao = questionary.Choice(marca.nome, marca.id)
        opcoes_marcas_para_escolher.append(opcao)

    id_marca_escolhida = questionary.select("Escolha a marca", opcoes_marcas_para_escolher).ask()

    nome = questionary.text("Digite o nome do modelo").ask()
    cadastrar(id_marca_escolhida, nome)
