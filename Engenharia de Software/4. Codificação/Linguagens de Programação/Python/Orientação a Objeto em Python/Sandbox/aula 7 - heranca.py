import rich

class Pessoa():
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self, aluno, curso):
        return f"Matrícula do {aluno} no curso {curso} feita!"

class Eletiva1(Aluno):
    def __init__(self, nome, idade, curso, turma, papel):
        super().__init__(nome, idade, curso, turma)
        self.papel = papel

membro2 = Eletiva1("Gabi", 22, "Engenharia da Computação", "B", "Infra")
rich.inspect(membro2)

if isinstance(membro2, Eletiva1):
    print("membro2 é uma instância de Eletiva1")
if isinstance(membro2, Pessoa):
    print("membro2 também é instancia de Pessoa!")