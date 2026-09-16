---
Fonte: Autoria Própria Rea
---
# Tuplas

Estrutura de dados ordenada, ==imutável== e indexada, capaz de armazenar múltiplos valores, ==inclusive de tipos diferentes==.

> Tupla → ordenada + imutável + indexada + iterável + permite valores duplicados.

É uma estrutura de dados adequada quando você precisa manter uma coleção ordenada de elementos que ==não deve ser modificada== após sua criação.

```python
frutas = ("maçã", "banana", "laranja")
```

## 1. Criação

```python
tupla = ()
numeros = (1, 2, 3, 4)
misturada = (10, "Python", True, 3.14)
```

Os parênteses podem ser omitidos quando a estrutura é claramente uma tupla:

```python
numeros = 1, 2, 3, 4
```

Também é possível criar uma tupla a partir de outro iterável:

```python
tupla = tuple("Python")
# ('P', 'y', 't', 'h', 'o', 'n')
```

Para criar uma tupla com apenas um elemento, é necessário utilizar uma vírgula:

```python
tupla = (10,)
```

Sem a vírgula, os parênteses representam apenas agrupamento:

```python
tupla = (10)
# 10
```

## 2. Fatiamento

Permite obter uma parte da tupla.

Sintaxe:

```python
tupla[início:fim:passo]
```

```python
numeros = (0, 1, 2, 3, 4, 5)

numeros[1:4]   # (1, 2, 3)
numeros[:3]    # (0, 1, 2)
numeros[3:]    # (3, 4, 5)
numeros[::2]   # (0, 2, 4)
numeros[::-1]  # (5, 4, 3, 2, 1, 0)
```

==O índice fim não é incluído==.

## 3. Acesso aos elementos

Tuplas são ==imutáveis==, portanto seus elementos não podem ser modificados após a criação.

```python
frutas = ("maçã", "banana", "laranja")

frutas[1]
# "banana"
```

Tentativas de alteração geram `TypeError`:

```python
frutas[1] = "uva"
# TypeError
```

Para obter uma nova tupla com alterações, é necessário criar outra tupla:

```python
frutas = ("maçã", "banana", "laranja")

frutas = ("maçã", "uva", "laranja")
```

# Métodos para Tuplas

As tuplas possuem ==menos métodos que as listas==, principalmente porque são imutáveis.

## 1. Pesquisa

### in

Verifica se um elemento existe:

```python
"banana" in frutas
```

### index()

Obtém a posição de um elemento:

```python
frutas.index("banana")
```

### count()

Conta quantas vezes um elemento aparece:

```python
numeros.count(10)
```

## 2. Tamanho

`len()` retorna a quantidade de elementos:

```python
len(frutas)
```

## 3. Ordenação

Tuplas não possuem `sort()`, pois são ==imutáveis==.

É possível utilizar `sorted()`, que retorna uma ==nova lista ordenada==:

```python
numeros = (3, 1, 2)

ordenados = sorted(numeros)
# [1, 2, 3]
```

Caso seja necessário obter outra tupla:

```python
ordenados = tuple(sorted(numeros))
# (1, 2, 3)
```

# Iteração

Tuplas são iteráveis:

```python
for fruta in frutas:
    print(fruta)
```

Com índice:

```python
for i, fruta in enumerate(frutas):
    print(i, fruta)
```

# Tuple Comprehension

==Não existe tuple comprehension em Python.==

Uma expressão semelhante utilizando parênteses cria um ==generator expression==:

```python
quadrados = (x ** 2 for x in range(5))
```

Para obter uma tupla, é necessário convertê-la:

```python
quadrados = tuple(x ** 2 for x in range(5))
```

Resultado:

```python
(0, 1, 4, 9, 16)
```

Com condição:

```python
pares = tuple(x for x in range(10) if x % 2 == 0)
```

> List comprehension → `[expressão for ...]`
> 
> Generator expression → `(expressão for ...)`
> 
> Tupla → `tuple(iterável)`

# Operações com tuplas

### Concatenação

```python
a = (1, 2)
b = (3, 4)

c = a + b
# (1, 2, 3, 4)
```

### Repetição

```python
tupla = (0,) * 5
# (0, 0, 0, 0, 0)
```

### Comparação

Tuplas podem ser comparadas elemento a elemento:

```python
(1, 2) == (1, 2)  # True
(1, 2) == (2, 1)  # False
```

A ordem dos elementos importa.

Também é possível utilizar operadores relacionais:

```python
(1, 2) < (1, 3)  # True
```

# Desempacotamento

Tuplas são frequentemente utilizadas para ==desempacotar valores== em diferentes variáveis:

```python
ponto = (10, 20)

x, y = ponto

print(x)  # 10
print(y)  # 20
```

Também é possível utilizar `*` para capturar múltiplos elementos:

```python
numeros = (1, 2, 3, 4, 5)

primeiro, *meio, ultimo = numeros

# primeiro → 1
# meio     → [2, 3, 4]
# ultimo   → 5
```

# Cópia

Como tuplas são ==imutáveis==, geralmente não é necessário criar cópias para evitar alterações acidentais.

Ao atribuir uma tupla a outra variável:

```python
a = (1, 2, 3)
b = a
```

`a` e `b` referenciam a ==mesma tupla==, mas isso não permite modificar a estrutura.

É possível utilizar:

```python
b = tuple(a)
```

Porém, para uma tupla já existente, isso normalmente não é necessário.

# Tuplas aninhadas

Uma tupla pode conter outras tuplas:

```python
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
```

Acesso:

```python
matriz[0][1]
# 2
```

Tuplas também podem conter listas ou outros objetos mutáveis:

```python
dados = (
    "Python",
    [1, 2, 3]
)
```

Nesse caso, a ==tupla continua imutável==, mas a lista armazenada nela pode ser modificada:

```python
dados[1].append(4)

# ("Python", [1, 2, 3, 4])
```

Portanto, a imutabilidade da tupla impede a alteração de seus ==elementos/referências==, mas não necessariamente dos objetos mutáveis armazenados dentro dela.