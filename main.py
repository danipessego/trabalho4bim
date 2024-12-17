# Trabalho: Sistemas de Integração de Atividades Extracurriculares e Complementares
# Equipe: Eevee
# Disciplina: Programação Orientada a Objeto
# Alunos: Ana Clara, Anna Flávia, Arthur Miranda, e Maria Daniella
# 2 informática Matutino

from classes import *
from outros import *

# Lista de Estudantes
estudantes = []

# Funções
# Exibe as turmas disponíveis
def mostrar_opcoes_turmas():
    print("Opções de Turmas:")
    for turma in turmas_disponiveis:
        print(f"{turma.nome} [{turma.numero}]")
# Exibe os esportes disponíveis
def mostrar_opcoes_esporte():
    print("Opções de Esportes:")
    for esporte, horario in esportes.items():
        print(f"{esporte}: {horario}")
# Exibe as turmas do Centro de Idiomas disponíveis
def mostrar_opcoes_idioma():
    print("Opções de Idiomas:")
    for turma in turmas_idiomas:
        print(f"{turma.nome} [{turma.numero}] - {turma.horario}")
# Exibe os projetos disponíveis
def mostrar_opcoes_projeto():
    print("Opções de Projetos:")
    for projeto, horario in projetos.items():
        print(f"{projeto}: {horario}")
# Cadastra os Estudantes
def cadastrar_estudante():
    nome = input("Digite o nome do aluno: ")
    senha = input("Digite a senha do aluno: ")

    mostrar_opcoes_turmas()
# Tratamento de exceção na escolha de turma
    try:
        turma_numero = int(input("Escolha uma turma pelo número: "))
        turma_selecionada = next((turma for turma in turmas_disponiveis if turma.numero == turma_numero), None)
        if turma_selecionada is None:
            raise ValueError("Turma inválida.")
    except ValueError as e:
        print("Turma inválida! Tente Novamente")
        return

    estudante = Estudante(nome, senha, turma_selecionada.nome)

    # Cadastro Estudante atleta
    escolha = input("Deseja cadastrar um esporte? (digite s para SIM e n para NÃO): ").strip().lower()
    if escolha == 's':
        mostrar_opcoes_esporte()
        esporte = input("Escolha um esporte: ")
        if esporte in esportes:
            estudante.esporte = esporte

    # Cadastro Estudante do centro de idiomas
    escolha = input("Deseja cadastrar um idioma? (digite s para SIM e n para NÃO): ").strip().lower()
    if escolha == 's':
        mostrar_opcoes_idioma()
        idioma_numero = int(input("Escolha um idioma pelo código: "))
        turma_idioma = next((turma for turma in turmas_idiomas if turma.numero == idioma_numero), None)
        if turma_idioma:
            estudante.idioma = turma_idioma.nome

    # Cadastro Estudante de projeto
    escolha = input("Deseja cadastrar um projeto? (digite s para SIM e n para NÃO): ").strip().lower()
    if escolha == 's':
        mostrar_opcoes_projeto()
        projeto = input("Escolha um projeto: ")
        if projeto in projetos:
            estudante.projeto = projeto

    estudantes.append(estudante)
    print("Cadastro realizado com sucesso!")
    print(estudante)

def login():
    nome = input("Digite o nome do aluno: ")
    senha = input("Digite a senha do aluno: ")
    for estudante in estudantes:
        if estudante.nome == nome and estudante.senha == senha:
            print("Login bem-sucedido!")
            print(estudante)
            return
    print("Nome ou senha incorreta.")
    
# Interface
def main():
    while True:
        print("\n1. Login")
        print("2. Cadastro")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            login()
        elif opcao == '2':
            cadastrar_estudante()
        elif opcao == '3':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
