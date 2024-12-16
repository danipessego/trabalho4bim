# Trabalho: Sistemas de Integração de Atividades Extracurriculares e Complementares
# Equipe: Eevee
# Disciplina: Programação Orientada a Objeto
# Alunos: Ana Clara, Anna Flávia, Arthur Miranda, e Maria Daniella
# 2 informática Matutino

# Listas de turma, esportes e das turmas do Centro de Idiomas (nomeamos de idiomas)
# A lista armazena as turmas disponíveis

class Turma:
    def __init__(self, nome, numero, horario=None):
        self.nome = nome
        self.numero = numero
        self.horario = horario

    def __str__(self):
        return f"{self.nome} - {self.horario}" if self.horario else self.nome

turmas_disponiveis = [
    Turma("1 A informática", 1), Turma("1 B informática", 2), Turma("2 A informática", 3), Turma("2 B informática", 4), Turma("3 A informática", 5), Turma("3 B informática", 6),
    Turma("1 A eletrotécnica", 7), Turma("1 B eletrotécnica", 8), Turma("2 A eletrotécnica", 9), Turma("2 B eletrotécnica", 10), Turma("3 A eletrotécnica", 11), Turma("3 B eletrotécnica", 12),
    Turma("1 A edificações", 13), Turma("1 B edificações", 14), Turma("2 A edificações", 15), Turma("2 B edificações", 16), Turma("3 A edificações", 17), Turma("3 B edificações", 18),
    Turma("1 A química", 19), Turma("1 B química", 20), Turma("2 A química", 21), Turma("2 B química", 22), Turma("3 A química", 23), Turma("3 B química", 24)
]
# A lista armazena os esportes disponíveis
esportes = {
    "Futsal": "Segunda e Quarta, 19h até 20h30",
    "Basquete": "Quarta e Sexta, 18h30 até 20h30",
    "Vôlei": "Terça e Quinta, 18h30 até 21h",
    "Handebol": "Segunda e Quinta, 19h até 20h30"
}
# A lista armazena as turmas do centro de idiomas disponíveis
turmas_idiomas = [
    Turma("Inglês - Básico", 1, "Segunda e Quarta, 15h até 16h"),
    Turma("Espanhol - Básico", 2, "Segunda e Quarta, 15h até 16h"),
    Turma("Inglês - Intermediário", 3, "Terça e Quinta, 15h até 16h"),
    Turma("Espanhol - Intermediário", 4, "Terça e Quinta, 15h até 16h"),
    Turma("Inglês - Avançado", 5, "Segunda e Quarta, 16h até 17h"),
    Turma("Espanhol - Avançado", 6, "Terça e Quinta, 16h até 17h")
]
# A lista armazena os projetos disponíveis
projetos = {
    "Biogirls": "Segunda e Quarta, 14h até 17h",
    "Robótica": "Quarta e Sexta, 14h até 17h",
    "Astrogenitas": "Terça e Quinta, 14h até 17h",
    "Audiotrap": "Segunda e Quinta, 14h até 17h"
}
