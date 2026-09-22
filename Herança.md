---
Fonte 1: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# Herança
É um relacionamento do tipo entre ==itens gerais== (*ancestrais*) e ==tipos mais específicos== (*descendentes*) desses itens, que herdam **atributos** e **métodos** dos níveis superiores.


Uma Classe Filha não apenas irá herdaros atributos e métodos, mas ==também pode ter os seus próprios==!
![[Pasted image 20260916213533.png | 200]]![[Pasted image 20260916213643.png | 150]] ![[Pasted image 20260916214206.png | 400]]



![[Sem título 1.png]]


Sempre devemos usar a seta vazia para simbolizar Herança.

Aluno, professor e funcionário herdam da classe Pessoa.


`é um`
Aluno **é um**a pessoa
Professor **é um**a pessoa
Funcionário **é um**a pessoa



`Principais vantagens`:
- Reutilização de código
- Organização hierárquica
- Facilita manutenção

```python
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
```