---
Fonte: Autoria Própria Rea
---
# Conjuntos

Estrutura de dados ==mutável==, não ordenada e iterável, capaz de armazenar múltiplos valores, ==sem permitir elementos duplicados==.

> Conjunto → não ordenado + mutável + iterável + não permite valores duplicados.

É uma estrutura de dados particularmente adequada quando você precisa trabalhar com ==elementos únicos== ou realizar operações matemáticas de conjuntos, como união, interseção e diferença.

```python
frutas = {"maçã", "banana", "laranja"}
```

## 1. Criação

```python
conjunto = set()
numeros = {1, 2, 3, 4}
misturado = {10, "Python", True, 3.14}
```

==`{}` cria um dicionário vazio, não um conjunto vazio==:

```python
vazio = {}
# dicionário
```

Para criar um conjunto vazio:

```python
vazio = set()
```

Também é possível criar um conjunto a partir de outro iterável:

```python
conjunto = set([1, 2, 2, 3])
# {1, 2, 3}
```

Elementos duplicados são ==automaticamente removidos==:

```python
numeros = {1, 2, 2, 3, 3, 3}
# {1, 2, 3}
```

## 2. Acesso aos elementos

Conjuntos não possuem índices, pois são ==não ordenados==.

Portanto, isto não é permitido:

```python
frutas[0]
# TypeError
```

Para verificar se um elemento existe:

```python
"banana" in frutas
```

A principal forma de percorrer os elementos é por meio de iteração:

```python
for fruta in frutas:
    print(fruta)
```

==A ordem dos elementos não deve ser considerada garantida==.

# Métodos para Conjuntos

## 1. Adição de elementos

### add()

Adiciona um elemento:

```python
frutas.add("uva")
```

Se o elemento já existir, o conjunto permanece inalterado:

```python
frutas.add("banana")
```

### update()

Adiciona vários elementos a partir de um iterável:

```python
frutas.update(["uva", "manga"])
```

Também pode receber vários iteráveis:

```python
frutas.update(["uva"], {"manga", "pera"})
```

## 2. Remoção de elementos

### remove()

Remove um elemento:

```python
frutas.remove("banana")
```

Se o elemento não existir, ocorre `KeyError`.

### discard()

Remove um elemento, mas ==não gera erro== caso ele não exista:

```python
frutas.discard("banana")
```

### pop()

Remove e retorna um elemento ==arbitrário==:

```python
fruta = frutas.pop()
```

Como conjuntos não são ordenados, não é possível determinar qual elemento será removido.

### clear()

Remove todos os elementos:

```python
frutas.clear()
```

# Operações com Conjuntos

## 1. União

Combina os elementos de dois conjuntos, ==eliminando duplicados==.

### union()

```python
a = {1, 2, 3}
b = {3, 4, 5}

c = a.union(b)
# {1, 2, 3, 4, 5}
```

Também é possível utilizar o operador `|`:

```python
c = a | b
```

## 2. Interseção

Obtém os elementos ==presentes nos dois conjuntos==.

### intersection()

```python
a = {1, 2, 3}
b = {2, 3, 4}

c = a.intersection(b)
# {2, 3}
```

Também é possível utilizar o operador `&`:

```python
c = a & b
```

## 3. Diferença

Obtém os elementos que estão no ==primeiro conjunto, mas não no segundo==.

### difference()

```python
a = {1, 2, 3}
b = {2, 3, 4}

c = a.difference(b)
# {1}
```

Também é possível utilizar o operador `-`:

```python
c = a - b
```

A ordem importa:

```python
a - b
# {1}

b - a
# {4}
```

## 4. Diferença simétrica

Obtém os elementos que estão em ==apenas um dos dois conjuntos==.

### symmetric_difference()

```python
a = {1, 2, 3}
b = {2, 3, 4}

c = a.symmetric_difference(b)
# {1, 4}
```

Também é possível utilizar o operador `^`:

```python
c = a ^ b
```

## 5. Subconjunto

Verifica se todos os elementos de um conjunto estão contidos em outro.

### issubset()

```python
a = {1, 2}
b = {1, 2, 3}

a.issubset(b)
# True
```

Também é possível utilizar `<=`:

```python
a <= b
# True
```

## 6. Superconjunto

Verifica se um conjunto contém todos os elementos de outro.

### issuperset()

```python
a = {1, 2, 3}
b = {1, 2}

a.issuperset(b)
# True
```

Também é possível utilizar `>=`:

```python
a >= b
# True
```

## 7. Conjuntos disjuntos

### isdisjoint()

Verifica se dois conjuntos ==não possuem elementos em comum==:

```python
a = {1, 2}
b = {3, 4}

a.isdisjoint(b)
# True
```

# Pesquisa

### in

Verifica se um elemento pertence ao conjunto:

```python
"banana" in frutas
```

### not in

Verifica se um elemento não pertence ao conjunto:

```python
"banana" not in frutas
```

# Tamanho

`len()` retorna a quantidade de elementos:

```python
len(frutas)
```

Como conjuntos não permitem duplicatas, cada elemento é contado ==uma única vez==:

```python
numeros = {1, 1, 2, 2, 3}

len(numeros)
# 3
```

# Iteração

Conjuntos são iteráveis:

```python
for fruta in frutas:
    print(fruta)
```

É possível utilizar `enumerate()`, mas o índice representa apenas a posição da iteração, ==não uma posição fixa do conjunto==:

```python
for i, fruta in enumerate(frutas):
    print(i, fruta)
```

# Set Comprehension

Forma compacta de criar conjuntos a partir de uma expressão e, opcionalmente, uma condição.

```python
quadrados = {x ** 2 for x in range(5)}
```

Resultado:

```python
{0, 1, 4, 9, 16}
```

Com condição:

```python
pares = {
    x
    for x in range(10)
    if x % 2 == 0
}
```

Elementos duplicados continuam sendo ==automaticamente eliminados==:

```python
quadrados = {x ** 2 for x in [1, 1, 2, 2, 3]}

# {1, 4, 9}
```

# Cópia

Cuidado ao atribuir um conjunto a outra variável:

```python
a = {1, 2, 3}
b = a
```

Nesse caso, `a` e `b` referenciam o ==mesmo conjunto==.

Para criar uma cópia:

```python
b = a.copy()
```

ou:

```python
b = set(a)
```

Essas formas criam uma ==cópia superficial==.

Para estruturas aninhadas, pode ser necessário `copy.deepcopy()`.

# Frozen Set

`frozenset` é uma versão ==imutável== de um conjunto:

```python
numeros = frozenset({1, 2, 3})
```

Não permite operações que alterem o conjunto:

```python
numeros.add(4)
# AttributeError
```

Por ser imutável e hashable, um `frozenset` pode ser utilizado como ==chave de dicionário== ou como elemento de outro conjunto:

```python
dados = {
    frozenset({1, 2}): "valores"
}
```

A maioria das operações de conjuntos também pode ser utilizada com `frozenset`.