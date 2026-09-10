---
Fonte: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# __ dict __
Atributo especial que funciona como um ==dicionário armazenando automaticamente todos os atributos de um objeto==, servindo como uma representação padrão da estrutura interna da instância.

É *imutável*.

```python
class MinhaClasse():
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

obj = MinhaClasse("Renan", 25)

print(obj.__dict__)
```
## Diferença do __ getstate __
**O __ getstate __ é um método que oferece flexibilidade** ao desenvolvedor, permitindo filtrar, formatar ou selecionar quais informações específicas devem ser expostas.