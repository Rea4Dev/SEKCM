---
Fonte 1: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# __ self __
É um ==atributo de instância==, ou seja, ele faz sentido quando você pensa na instância.

Como mostrado no vídeo, observe que o self funciona como um identificador para a *própria instância* que está executando o método. 

Ele garante que, ao chamar uma funcionalidade, como o método **aniversario()**, a alteração seja feita apenas no objeto específico que realizou a chamada.

Em termos práticos:
* Quando você escreve `self.nome` ou `self.idade` dentro da classe, o Python substitui o `self` pelo nome do objeto que invocou o método no momento da execução.
* Isso permite que múltiplos objetos coexistam e mantenham seus próprios **dados individuais** sem interferir nos valores uns dos outros.