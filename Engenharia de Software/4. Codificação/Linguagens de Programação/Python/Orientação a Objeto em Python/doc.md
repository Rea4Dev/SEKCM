---
Fonte: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# __ doc __
O **__doc__** (ou *dunder doc*) é um **atributo especial** utilizado para acessar a documentação interna de uma classe, função ou módulo.

Ele armazena a **docstring**, que é o texto explicativo definido entre três aspas logo abaixo da declaração de uma **classe** ou método, servindo como um manual de instruções para outros desenvolvedores.

Ao utilizar esse atributo, o *Python* permite consultar rapidamente para que serve aquele objeto, facilitando a manutenção e a compreensão do **código** sem a necessidade de acessar o arquivo fonte original.

```python
class MinhaClasse():
	"""
	Docstring.
	"""
	pass

obj = MinhaClasse()

print(obj.__doc__)
```