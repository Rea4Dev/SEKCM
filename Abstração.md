---
Fonte: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# Abstração
- Existe a ==abstração de dados==, que acontece quando ignoramos informações desnecessárias para o escopo do projeto.
- Existe a ==abstração de processos==, quando não precisamos saber como um método faz seu trabalho, apenas sabe que ele existe pela *interface*.


Para entender melhor, pense no uso de um Controle Remoto:

![[Pasted image 20260920014131.png | 250]] ![[Pasted image 20260920014401.png | 223]] ![[Pasted image 20260920014951.png | 233]]

Isso é abstração!
Dessa maneira, o usuário ==não precisa saber detalhes da implementação== e passa a se focar apenas na *interface pública* que está ali disponível.

Para uma função built-in, como o print(), não precisamos saber como ela funciona exatamente. 

## Vantagens da Abstração
- ==Maior legibilidade==: Você consegue entender melhor um código se você abstrai os detalhes. Os métodos estarão dentro do módulo, você só precisa entender como chamá-los.
- ==Padronização==: Ao usar a abstração, você define um ==contrato==. Todas as *subclasses (filhas) de uma classe abstrata são obrigatoriamente forçadas a implementar* as mesmas funcionalidades, garantindo que o sistema siga um padrão consistente.
- ==Simplicidade==: Ajuda a simplificar problemas grandes, tornando softwares complexos mais fáceis de manter e entender.
- ==Segurança==:  Ao não expor os detalhes internos de funcionamento (como os "circuitos" internos de um controle), você evita o uso indevido e protege a integridade do código, trabalhando em conjunto com o pilar de Encapsulamento.



## Malefícios da não-abstração`
Pense que você vai criar uma classe aluno, e então pensa:

- Aluno tem nome, tamanho, peso, cor, nacionalidade, cor preferida, comida favorita (...)
- Aluno pode andar, comer, tossir, respirar, sentar, olhar, anotar, abrir mochila (...)

Os exemplos acima, embora hiperbólicos, representam exatamente o escopo de necessidade de abstração. Sem abstrair, você `escreve mais código`, `gasta mais tempo`, `atrasa o lançamento do sistema`. 


É ==inviável focar no irrelevante==. *Devemos abstrair, focar somente no essencial* para a situação.



# Classe Abstrata
Todos os controles remotos possuem ==funcionalidades essenciais em comum==, como ligar/desligar, ajustar volume e mudar canais. Mesmo que *a implementação interna de como cada modelo envia o sinal para a televisão seja diferente*, a **interface** para o usuário é padronizada.

Podemos criar uma classe mãe (abstrata), como "Controle Remoto Genérico", que estabelece um contrato contendo esses métodos. ==As classes filhas (controles de marcas ou aparelhos específicos) herdam essa estrutura e são obrigadas a implementar a lógica específica para cada botão==, garantindo que o comportamento esperado esteja presente em qualquer controle derivado. 

Não há como, na classe mãe "Controle Remoto Genérico", definir como será o funcionamento dos métodos "ligar/desligar", haja vista que isso mudará para cada classe filha.


![[Pasted image 20260920144141.png]]

![[Sem título 3.png]]

- *Classe Abstrata*: classe que não vai servir para gerar objetos (nunca será instanciada), e sim ==funcionar como uma base para todas as subclasses se transformarem em objetos==.

	- *Método Concreto*: quando na classe abstrata, são métodos que terão o exato mesmo código para as demais subclasses. Desta forma, já sendo definido aqui.
	- *Métodos Abstratos*: é um ==método que está na classe mãe (classe abstrata)== que serve como um **contrato**, definindo o que as classes filhas deverão obrigatoriamente ter como método implementado (especializado).

![[Pasted image 20260920151451.png | 250]] ![[Pasted image 20260920151556.png | 220]] ![[Pasted image 20260920151919.png | 220]]



```python
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
```

