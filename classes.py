# Trabalho: Sistemas de Integração de Atividades Extracurriculares e Complementares
# Equipe: Eevee
# Disciplina: Programação Orientada a Objeto
# Alunos: Ana Clara, Anna Flávia, Arthur Miranda, e Maria Daniella
# 2 informática Matutino

# Relacionamento de Composição logo abaixo
# Classe tod0

from main import *
class Estudante:
    def __init__(self, nome, senha, turma=None, esporte=None, idioma=None, projeto=None):
        self.nome = nome
        self.senha = senha
        self.turma = turma
        self.esporte = esporte
        self.idioma = idioma
        self.projeto = projeto

    def __str__(self):
        info = f"Nome: {self.nome}, Turma: {self.turma}"
        if self.esporte:
            info += f", Esporte: {self.esporte} - Horário: {esportes[self.esporte]}"
        if self.idioma:
            info += f", Idioma: {self.idioma} - Horário: {next(turma.horario for turma in turmas_idiomas if turma.nome == self.idioma)}"
        if self.projeto:
            info += f", Projeto: {self.projeto} - Horário: {projetos[self.projeto]}"
        return info

# Classe parte
class Turma:
    def __init__(self, nome, numero, horario=None):
        self.nome = nome
        self.numero = numero
        self.horario = horario

    def __str__(self):
        return f"{self.nome} - {self.horario}" if self.horario else self.nome
