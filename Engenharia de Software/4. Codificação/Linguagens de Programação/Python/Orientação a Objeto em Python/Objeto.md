---
Fonte: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# O que é um Objeto
Coisa ==concreta== ou ==abstrata== que é feita a partir de um ==molde== <small style="font-size: 80%; color: grey;">(classe)</small> e pode ser descrita por meio das suas *características* <small style="font-size: 80%; color: grey;">(atributos)</small>, *comportamentos* <small style="font-size: 80%; color: grey;">(métodos)</small> e *estado* atual.
![[Pasted image 20260813200740.png | center | 300]]
# Objetos Abstratos
Um objeto abstrato é uma ==entidade que não possui existência física== (não é algo que você consegue pegar ou tocar no mundo real), mas que *é tratada como um objeto dentro de um sistema de software*. 
Assim como os objetos concretos, eles possuem atributos (características) e métodos (comportamentos) definidos por uma classe.

>[!Tip] Abstrato vs Concreto
>Seja preciosista na hora de categorizar. 
>- Um *objeto concreto* é algo que, naturalmente, é de fato um objeto.
>	- Biscoito.
>	- Carro.
><br>
>- Já um *objeto abstrato*, é algo da vida real que é REPRESENTADO como um objeto para ser manipulado por um sistema OO.
>	- **Consulta Médica:** Atributos como endereço, médico responsável e horário; métodos como iniciar, cancelar ou adiar consulta.
>	- **Processo de Venda:** Atributos como valor e produto; métodos como iniciar venda e receber pagamento.
>	- **Erro no Sistema:** Um conceito muito importante em programação. Atributos incluem código do erro e causa; métodos incluem disparar ou corrigir o erro.

# Estado do Objeto
Após ser instanciado, um <span style="color: green;">objeto</span> possui um **estado atual**, que é o ==conjunto de valores== que seus ==atributos== possuem em um ==determinado momento==. Esse estado *pode mudar com o passar do tempo ou por meio da execução de seus métodos* (ex: assar, morder, esfriar).

## Analogia da forma e do biscoito

É como se o estado do objeto fosse a foto do biscoito. 
Ou então, o ponto na linha do tempo daquele biscoito.
![[Pasted image 20260825192626.png | center | 400]]
Veja que, caso eu execute o método ==morder()==, por exemplo, o atributo peso mudaria. *Chamamos de estado o conjunto de valores dos atributos naquele momento*.

---
> Parte 2 (recomendado após ver parte 2 de classe).

# Declaração de Objeto
![[Pasted image 20260831180606.png]]

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