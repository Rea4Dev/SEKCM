---
Fonte: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# Método __ getstate __
Método especial que ==permite personalizar a forma como o estado interno== de um objeto é extraído ou exibido.

Diferente de uma exibição automática, ao sobrescrever este método, o desenvolvedor ganha controle total sobre quais atributos ou informações relevantes devem ser retornados quando o estado do objeto é solicitado.

```python
class MinhaClasse():
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade
	
	def __getstate__(self):
		return f"Estado: nome = {self.nome} ; idade = {self.idade}"

obj = MinhaClasse("Renan", 25)

print(obj.__getstate__())
```
## Diferença do __ dict __
__ dict __ funciona como um *atributo especial* (dicionário) que armazena automaticamente todos os atributos de um objeto, ele é uma representação padrão **fixa e não alterável**.