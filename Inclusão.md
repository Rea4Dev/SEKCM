---
Fonte: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# Polimorfismo de Inclusão (Override / Subtyping)
O polimorfismo de inclusão (também chamado de subtyping ou sobrescrita) ocorre quando ==uma subclasse define um método com o mesmo nome e assinatura que um método presente na sua superclasse==. Essa técnica *permite que o objeto da classe filha forneça uma implementação especializada do comportamento herdado*, sobrescrevendo a versão original definida pela classe mãe.

![[Pasted image 20260924214707.png]]

```python
class Mae:

    def __init__(self, nome):
        self.nome = nome

    def fazer_pudim(self):
        print("\nFaz pudim com leite condensado e calda")

    def fazer_coxinha(self):
        print("\nFrita a coxinha no óleo de soja")


class Filha(Mae):

    def fazer_pudim(self):
        print("\nEU SOU MENINA E FAÇO DIFERENTE!")


class Filho(Mae):

    def fazer_coxinha(self):
        print("\nEU SOU MENINO E FAÇO DIFERENTE!")


p1 = Mae("mother")
p1.fazer_pudim()
p1.fazer_coxinha()


p2 = Filho("son")
p2.fazer_pudim()
p2.fazer_coxinha()


p3 = Filha("daughter")
p3.fazer_pudim()
p3.fazer_coxinha()
```