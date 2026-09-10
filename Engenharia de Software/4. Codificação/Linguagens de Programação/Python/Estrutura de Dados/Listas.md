---
Fonte 1: Autoria Própria Rea
---
# Listas

Estrutura de dados ordenada, ==mutável== e indexada, capaz de armazenar múltiplos valores, ==inclusive de tipos diferentes==.

> Lista → ordenada + mutável + indexada + iterável + permite valores duplicados.

É uma das estruturas de dados mais utilizadas em Python e é particularmente adequada quando você precisa manter uma coleção ordenada de elementos que pode ser modificada.

```python
frutas = ["maçã", "banana", "laranja"]
```

## 1. Criação
```python
lista = []
numeros = [1, 2, 3, 4]
misturada = [10, "Python", True, 3.14]
```

Também é possível criar uma lista a partir de outro iterável:
```python
lista = list("Python")
# ['P', 'y', 't', 'h', 'o', 'n']
```

## 2. Fatiamento
Permite obter uma parte da lista

Sintaxe:
```python
lista[início:fim:passo]
```

```python
numeros = [0, 1, 2, 3, 4, 5]

numeros[1:4]   # [1, 2, 3]
numeros[:3]    # [0, 1, 2]
numeros[3:]    # [3, 4, 5]
numeros[::2]   # [0, 2, 4]
numeros[::-1]  # [5, 4, 3, 2, 1, 0]
```

==O índice fim não é incluído==.

## 3. Alteração de elementos
Listas são ==mutáveis==, portanto seus elementos podem ser modificados.
```python
frutas = ["maçã", "banana", "laranja"]

frutas[1] = "uva"
# ["maçã", "uva", "laranja"]
```

Também é possível alterar vários elementos:
```python
numeros[1:3] = [10, 20]
```



# Métodos para Listas

## 1. Adição de elementos
### append()
Adiciona um elemento ao final:
```python
frutas.append("uva")
```

### insert()
Adiciona em uma posição específica:
```python
frutas.insert(1, "uva")
```

### extend()
Adiciona vários elementos:
```python
frutas.extend(["uva", "manga"])
```

Diferença importante:
```python
lista.append([4, 5])
# [1, 2, 3, [4, 5]]

lista.extend([4, 5])
# [1, 2, 3, 4, 5]
```

## 2. Remoção de elementos
### remove()
Remove pela **valor**:
```python
frutas.remove("banana")
```

### pop()
Remove pela **posição** e retorna o elemento removido:
```python
fruta = frutas.pop()
```

Ou:
```python
fruta = frutas.pop(1)
```

### del
Remove por índice ou intervalo:
```python
del frutas[1]
del frutas[1:3]
```

### clear()
Remove todos os elementos:
```python
frutas.clear()
```

## 3. Pesquisa
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

## 4. Tamanho
`len()` retorna a quantidade de elementos:
```python
len(frutas)
```

## 5. Ordenação
### sort()
Ordena a própria lista:
```python
numeros.sort()
```

Ordem decrescente:
```python
numeros.sort(reverse=True)
```

### sorted()
Cria uma **nova lista ordenada**, sem modificar a original:
```python
ordenados = sorted(numeros)
```

## 6. Inversão
### reverse()
Inverte a própria lista:
```python
frutas.reverse()
```

Também é possível usar slicing:
```python
invertida = frutas[::-1]
```



# Iteração
Listas são iteráveis:
```python
for fruta in frutas:
    print(fruta)
```

Com índice:
```python
for i, fruta in enumerate(frutas):
    print(i, fruta)
```



# List Comprehension
Forma compacta de criar listas a partir de uma expressão e, opcionalmente, uma condição.

```python
quadrados = [x ** 2 for x in range(5)]
```

Resultado:
```python
[0, 1, 4, 9, 16]
```

Com condição:
```python
pares = [x for x in range(10) if x % 2 == 0]
```



# Operações com listas
### Concatenação
```python
a = [1, 2]
b = [3, 4]

c = a + b
# [1, 2, 3, 4]
```

### Repetição
```python
lista = [0] * 5
# [0, 0, 0, 0, 0]
```

### Comparação
Listas podem ser comparadas elemento a elemento:

```python
[1, 2] == [1, 2]  # True
[1, 2] == [2, 1]  # False
```



# Cópia
Cuidado ao atribuir uma lista a outra variável:
```python
a = [1, 2, 3]
b = a
```

Nesse caso, `a` e `b` referenciam a **mesma lista**.

Para criar uma cópia:
```python
b = a.copy()
```

ou:
```python
b = a[:]
```

Para estruturas aninhadas, pode ser necessário `copy.deepcopy()`.


# Listas aninhadas
Uma lista pode conter outras listas:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Acesso:
```python
matriz[0][1]
# 2
```
