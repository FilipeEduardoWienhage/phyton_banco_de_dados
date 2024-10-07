import questionary
import os
from rich.console import Console
from rich.table import Table
from repositorios.cliente_repositorio import cadastrar, apagar, atualizar, obter_todos_clientes


def limpar_tela():
    os.system("cls")


def menu_clientes():
    opcao_escolhida = ""
    while opcao_escolhida != "Sair":
        opcao_escolhida = questionary.select(
        "Menu de Clientes",
        choices=[
            "Consultar clientes",
            "Cadastrar clientes",
            "Editar clientes",
            "Apagar clientes",
            "Sair"
        ]).ask()
        limpar_tela()

        if opcao_escolhida == "Consultar clientes":
            consultar_cliente()
        elif opcao_escolhida == "Cadastrar clientes":
            inserir_cliente()
        elif opcao_escolhida == "Editar clientes":
            atualizar_cliente()
        elif opcao_escolhida == "Apagar clientes":
            apagar_cliente()


def consultar_cliente():
    clientes = obter_todos_clientes()
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado")
        return
    
    table = Table(title="Consulta de Clientes")

    table.add_column("Código", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nome", justify="center", style="cyan", no_wrap=True)
    table.add_column("CPF/CNPJ", justify="center", style="cyan", no_wrap=True)
    table.add_column("Data de Nascimento", justify="center", style="cyan", no_wrap=True)
    table.add_column("e-mail", justify="center", style="magenta")
    table.add_column("Celular", justify="center", style="magenta")
    table.add_column("Estado", justify="center", style="magenta")
    table.add_column("Cidade", justify="center", style="magenta")
    table.add_column("Bairro", justify="center", style="green")
    table.add_column("Logradouro", justify="center", style="green")
    table.add_column("CEP", justify="center", style="green")
    table.add_column("Numero", justify="center", style="green")
    table.add_column("Complemento", justify="center", style="green")

    for cliente in clientes:
        table.add_row(str(cliente.id), cliente.nome, cliente.cpf_cnpj, str(cliente.data_nascimento), cliente.email, cliente.celular, cliente.estado, cliente.cidade, cliente.bairro, cliente.logradouro, cliente.cep, cliente.numero, cliente.complemento )

    console = Console()
    console.print(table)

    
def inserir_cliente():
    nome = questionary.text("Informe o nome do Cliente: ").ask()
    cpf_cnpj = questionary.text("Informe o cpf ou cnpj do Cliente: ").ask()
    data_nascimento = questionary.text("Informe a data de nascimento do Cliente: ").ask()
    email = questionary.text("Informe o e-mail do Cliente: ").ask()
    celular = questionary.text("Informe o celular do Cliente: ").ask()
    estado = questionary.text("Informe o estado do Cliente: ").ask()
    cidade = questionary.text("Informe a cidade do Cliente: ").ask()
    bairro = questionary.text("Informe o bairro do Cliente: ").ask()
    logradouro = questionary.text("Informe o logradouro do Cliente: ").ask()
    cep = questionary.text("Informe o cep do Cliente: ").ask()
    numero = questionary.text("Informe o numero da residencia do Cliente: ").ask()
    complemento = questionary.text("Informe o complemento da residencia: ").ask()
    cadastrar(nome, cpf_cnpj, data_nascimento, email, celular, estado, cidade, bairro, logradouro, cep, numero, complemento)
    print("Cliente cadastrado com sucesso")


def atualizar_cliente():
    clientes = obter_todos_clientes()
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado")
        return
    
    opcoes_para_escolher = []
    for cliente in clientes:
        opcao = questionary.Choice(cliente.nome, cliente.id)
        opcoes_para_escolher.append(opcao)

    id_cliente_escolhido = questionary.select(
        "Escolha o cliente para editar",
        choices=opcoes_para_escolher
    ).ask()

    nome_editado = questionary.text("Informe o nome: ").ask()
    cpf_cnpj_editado = questionary.text("Informe o CPF/CNPJ: ").ask()
    email_editado = questionary.text("Informe o email: ").ask()
    celular_editado = questionary.text("Informe o celular: ").ask()
    estado_editado = questionary.text("Informe o Estado: ").ask()
    cidade_editada = questionary.text("Informe a cidade: ").ask()
    bairro_editado = questionary.text("Informe o bairro: ").ask()
    logradouro_editado = questionary.text("Informe o logradouro: ").ask()
    cep_editado = questionary.text("Informe o CEP: ").ask()
    numero_editado = questionary.text("Informe o numero da residencia: ").ask()
    complemento_editado = questionary.text("Informe o complemento: ").ask()
    atualizar(nome_editado, cpf_cnpj_editado, email_editado, celular_editado, estado_editado, cidade_editada, bairro_editado, logradouro_editado, cep_editado, numero_editado, complemento_editado)


def apagar_cliente():
    clientes = obter_todos_clientes()
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado")
        return
    
    opcoes = []
    for cliente in clientes:
        opcao = questionary.Choice(cliente.nome, cliente.id)
        opcoes.append(opcao)

    id_apagar_cliente = questionary.select(
        "Escolha um Cliente para apagar",
        choices=opcoes,
    ).ask()
    apagar(id_apagar_cliente)
    