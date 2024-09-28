from typing import List
# O que é uma classe: classe é uma forma de representar uma coisa do mundo real em um objeto
class Pessoa:
    # nome e id são parâmetros

    # __init__ é o que chamamos de construtor, tem como objetivo construir
    # um objeto com os dados necessários para o funcionamente correto 
    def __init__(self, id: int, nome: str):
        # propriedades da classe
        self.id = id
        self.nome = nome
        self.altura = 0.0
        self.idade = 0 
        self.peso = 0.0



class Produto:
    def __init__(self, id: int, nome: str, preco_unitario: float, quantidade: int):
        self.id = id
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

def exemplo_com_lista_de_objetos():
    # criando uma lista de produtos, que será armazenado os objetos da classe produto
    produtos: List[Produto] = []

    # instanciando um objeto de produto chamado play_station
    play_station = Produto(1, "PlayStation 5 Pro", 6999.99, 1)
    # adicionar o produto na lista de produtos
    produtos.append(play_station)

    xbox_series_x = Produto(2, "Xbox Series X", 3500, 2)
    produtos.append(xbox_series_x)

    # for i in range(0, len(produtos)):
    #   produto = produtos[i]
    #   print(produto.nome)
    # Percorrendo a lista de produtos para apresentar
    for produto in produtos:
        total_produto = produto.preco_unitario * produto.quantidade
        print(produto.nome, total_produto)


def exemplo_com_classe():
    # instanciando um objeto chamado batatinha da classe pessoa
    francisco = Pessoa(1, "Francisco")
    # Definindo o valor para a propriedade altura que pertence ao objeto francisco
    francisco.altura = 1.72
    francisco.peso = 120
    francisco.idade = 30
    print(f"Id: {francisco.id}")
    print(f"Nome: {francisco.nome}")
    print(f"Altura: {francisco.altura}")
    print(f"Peso: {francisco.peso}")
    print(f"Idade: {francisco.idade}\n")

    william = Pessoa(2, "William")
    print(f"Id: {william.id}")
    print(f"Nome: {william.nome}")
    print(f"Altura: {william.altura}")
    print(f"Peso: {william.peso}")
    print(f"Idade: {william.idade}")


# Criar uma classe chamada aluno com id, nome, nota 1, nota2 e nota3
# Criar uma lista que contenha 3 alunos
# Apresentar o nome da cada aluno, média e se está aprovado ou não

class Aluno:
    def __init__(self, id: int, nome: str, nota1: float, nota2: float, nota3: float,):
        self.id = id
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

def lista_aluno():
    alunos: List[Aluno] = []

    spezia = Aluno(1, "Spezia", 8, 1, 5)
    alunos.append(spezia)

    filipe = Aluno(2, "Filipe", 10, 8, 9)
    alunos.append(filipe)

    leonardo = Aluno(3, "Leonardo", 8, 8, 8)
    alunos.append(leonardo)

    for aluno in alunos:
        media = (aluno.nota1 + aluno.nota2 + aluno.nota3) / 3
        print(aluno.nome, media) 

if __name__ == "__main__":
    lista_aluno()
