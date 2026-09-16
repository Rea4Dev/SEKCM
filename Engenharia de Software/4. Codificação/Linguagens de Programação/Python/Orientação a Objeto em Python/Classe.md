---
Fonte: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# O que é uma Classe
É uma estrutura que define as ==características== (atributos) e os ==comportamentos== (métodos) que os ==objetos de um determinado tipo== terão.

A partir de uma classe, podemos criar *diversos objetos que compartilham a mesma estrutura, mas podem possuir valores diferentes para seus atributos*.

Entretanto, **uma classe não é um objeto**.

![[Pasted image 20260812193550.png]]

## Analogia - Forma de Biscoito

Pensando em dois biscoitos (objetos) de mesmo formato, podemos ilustrar uma classe como sendo a forma.

Veja:
- Podemos ter SOMENTE a forma, sem ter nenhum biscoito.
- Se há biscoito, houve forma.
- Os biscoitos podem variar nos ingredientes (atributos), cor etc. Mas no fim, possuem o mesmo formato (são objetos da mesma classe) e a mesma funcionalidade (métodos).


# Diagrama de Classes UML - Determinando uma Classe antes de Codar
Em Sistemas Orientados a Objetos, ==na hora em que se vai determinar uma classe é preciso pensar como se quer o objeto no futuro==, e para isso é utilizado um *diagrama de classes UML* que informa três coisas:
1. Nome
2. Características (**atributos**)
3. Coisas que pode fazer ou ser feita com ela (**métodos**)
 ![[Pasted image 20260812195550.png | center | 250]]
 ---
> Parte 2 (recomendado após ver parte 1 de Instância e Objeto).
# Declarando uma Classe
![[Pasted image 20260831180633.png]]

```python
class Pessoa():             # Definindo
	def __init__(self):
	    self.nome = ""
	    self.idade = 0
	
	def niver(self):
		self.idade += 1
		
humano1 = Pessoa()         # Instanciando

humano1.nome = "Renan"     # Usando
humano1.niver()            # Usando (método tem parênteses, atributo não)

print(f"{humano1.nome} de {humano1.idade} anos")        # Consumindo
```

```python
class Pessoa():          
	def __init__(self, nome, idade = 0):
	    self.nome = nome
	    self.idade = idade
	
	def niver(self):
		self.idade += 1
		
humano1 = Pessoa("Renan", 25)         # Instanciando & usando
humano1.niver()

print(f"{humano1.nome} de {humano1.idade} anos")       
```