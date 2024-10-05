import questionary
import os
from rich.console import Console
from rich.table import Table
from repositorios.proprietario_repositorio import cadastrar, apagar, atualizar, obter_todos_proprietarios


def limpar_tela():
    os.system("cls")


def menu_proprietarios():
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select(
        "Menu de Proprietarios",
        choices=[
            "Consultar proprietarios",
            "Cadastrar proprietarios",
            "Editar proprietarios",
            "Apagar proprietarios",
            "Sair"
        ]).ask()
        limpar_tela()

        if opcao_escolhida == "Consultar proprietarios":
            consultar_proprietario()
        elif opcao_escolhida == "Cadastrar proprietarios":
            inserir_proprietario()
        elif opcao_escolhida == "Editar proprietarios":
            atualizar_proprietario()
        elif opcao_escolhida == "Apagar proprietarios":
            apagar_proprietario()


def consultar_proprietario():
    pass


def inserir_proprietario():
    nome = questionary.text("Informe o nome do proprietario: ").ask()
    cpf_cnpj = questionary.text("Informe o cpf ou cnpj do proprietario: ").ask()
    data_nascimento = questionary.text("Informe a data de nascimento do proprietario: ").ask()
    email = questionary.text("Informe o e-mail do proprietario: ").ask()
    celular = questionary.text("Informe o celular do proprietario: ").ask()
    estado = questionary.text("Informe o estado do proprietario: ").ask()
    cidade = questionary.text("Informe a cidade do proprietario: ").ask()
    bairro = questionary.text("Informe o bairro do proprietario: ").ask()
    logradouro = questionary.text("Informe o logradouro do proprietario: ").ask()
    cep = questionary.text("Informe o cep do proprietario: ").ask()
    numero = questionary.text("Informe o numero da residencia do proprietario: ").ask()
    complemento = questionary.text("Informe o complemento da residencia: ").ask()
    cadastrar(nome, cpf_cnpj, data_nascimento, email, celular, estado, cidade, bairro, logradouro, cep, numero, complemento)
    print("Proprietario cadastrado com sucesso")


def atualizar_proprietario():
    pass


def apagar_proprietario():
    pass