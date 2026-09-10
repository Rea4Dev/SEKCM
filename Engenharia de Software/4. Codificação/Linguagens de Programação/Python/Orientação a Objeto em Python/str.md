---
Fonte: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# __ str __
O  **__str__** é um recurso especial que permite personalizar a forma como um objeto é representado quando solicitamos a sua exibição, como ao usar a função print.

Em vez de mostrar o endereço de memória onde o objeto está alocado, ao sobrescrever este método dentro de uma **classe**, podemos definir uma string formatada que descreve os dados internos do objeto de maneira mais amigável e legível para o usuário.

Ele deve obrigatoriamente retornar uma **string** contendo a representação desejada, substituindo o comportamento padrão que geralmente é pouco informativo para quem está utilizando a classe.

```python
class MinhaClasse():
	def __init__(self):
		pass
	
	def __str__(self):
		return "Mensagem"

obj = MinhaClasse()

print(obj)
```