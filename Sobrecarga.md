---
Fonte: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# Polimorfismo de Sobrecarga (Ad-Hoc Overloading)
Existem dois tipos:
- Sobrecarga de Método
- Sobrecarga de Operador

## Sobrecarga de Método
>Necessário import de biblioteca built-in.

É quando temos ==vários métodos com o mesmo nome, mas dependendo do parâmetro iremos executar um método específico==.

Este comportamento é limitado a apenas **um parâmetro**.
![[Pasted image 20260924220712.png | center | 200]]
```python
from functools import singledispatchmethod


class Analisador:

    @singledispatchmethod
    def analisar(self, valor):
        print("Não foi possível.")

    @analisar.register
    def _(self, valor: int):
        print("É um inteiro")

    @analisar.register
    def _(self, valor: str):
        print("É uma string")


x = Analisador()

x.analisar(123)
x.analisar("abc")

```