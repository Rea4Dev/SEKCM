from abc import ABC, abstractmethod
from rich.traceback import install
install()


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, turma):
        super().__init__(nome, idade)
        self.turma = turma

    def estudar(self):
        return f"Estudando na turma {self.turma}"


class Funcionario(Pessoa):
    def __init__(self, nome, idade, empresa):
        super().__init__(nome, idade)
        self.empresa = empresa

    def estudar(self):
        return f"Estudando para aplicar na {self.empresa}"


renan = Funcionario("Renan Gabriel", 25, "Embraer")
print(renan.estudar())