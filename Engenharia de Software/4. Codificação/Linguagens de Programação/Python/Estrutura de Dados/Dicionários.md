---
Fonte: Autoria Própria Rea
---
# Dicionários

Estrutura de dados ==mutável== e baseada em pares de **chave e valor**, capaz de armazenar múltiplos valores, ==inclusive de tipos diferentes==.

> Dicionário → mutável + baseado em chave/valor + iterável + chaves únicas.

É uma estrutura de dados particularmente adequada quando você precisa associar ==chaves a valores== e acessar esses valores de forma direta.

```python
pessoa = {
    "nome": "João",
    "idade": 25,
    "ativo": True
}
```

## 1. Criação

```python
dicionario = {}
pessoa = {"nome": "João", "idade": 25}
misturado = {
    "nome": "Python",
    "versao": 3.14,
    "ativo": True
}
```

Também é possível criar um dicionário utilizando `dict()`:

```python
pessoa = dict(nome="João", idade=25)
```

As chaves devem ser ==hashable==, como `str`, `int`, `float`, `tuple` e `bool`.

```python
dados = {
    "nome": "João",
    1: "um",
    (10, 20): "ponto"
}
```

==Listas, dicionários e outros objetos mutáveis não podem ser utilizados como chaves==.

## 2. Acesso aos elementos

Os valores são acessados por meio de suas ==chaves==:

```python
pessoa = {
    "nome": "João",
    "idade": 25
}

pessoa["nome"]
# "João"
```

Caso a chave não exista, ocorre `KeyError`:

```python
pessoa["altura"]
# KeyError
```

Também é possível utilizar `get()`:

```python
pessoa.get("altura")
# None
```

Ou definir um valor padrão:

```python
pessoa.get("altura", 0)
# 0
```

## 3. Alteração de elementos

Dicionários são ==mutáveis==, portanto seus elementos podem ser adicionados, alterados ou removidos.

Alteração:

```python
pessoa["idade"] = 26
```

Adição:

```python
pessoa["altura"] = 1.80
```

Se a chave já existir, seu valor é ==substituído==.

Se não existir, um novo par chave/valor é ==adicionado==.

# Métodos para Dicionários

## 1. Adição e atualização

### update()

Adiciona ou atualiza vários elementos:

```python
pessoa.update({
    "idade": 26,
    "altura": 1.80
})
```

Também pode receber argumentos nomeados:

```python
pessoa.update(nome="Maria", idade=30)
```

### setdefault()

Retorna o valor de uma chave e, caso ela não exista, adiciona a chave com um valor padrão:

```python
pessoa.setdefault("idade", 0)
```

Se `"idade"` já existir, seu valor não será alterado.

## 2. Remoção de elementos

### pop()

Remove uma chave e retorna seu valor:

```python
idade = pessoa.pop("idade")
```

Também é possível fornecer um valor padrão caso a chave não exista:

```python
idade = pessoa.pop("idade", 0)
```

### popitem()

Remove e retorna o ==último par chave/valor==:

```python
item = pessoa.popitem()
```

Resultado:

```python
("altura", 1.80)
```

### del

Remove um elemento pela chave:

```python
del pessoa["idade"]
```

### clear()

Remove todos os elementos:

```python
pessoa.clear()
```

## 3. Pesquisa

### in

Verifica se uma ==chave== existe:

```python
"nome" in pessoa
```

Por padrão, `in` pesquisa as chaves, não os valores:

```python
"João" in pessoa
# False
```

Para pesquisar nos valores:

```python
"João" in pessoa.values()
```

### get()

Obtém o valor associado a uma chave sem gerar `KeyError` caso ela não exista:

```python
pessoa.get("nome")
```

## 4. Chaves e valores

### keys()

Retorna uma visão das chaves:

```python
pessoa.keys()
```

### values()

Retorna uma visão dos valores:

```python
pessoa.values()
```

### items()

Retorna uma visão dos pares chave/valor:

```python
pessoa.items()
```

Exemplo:

```python
for chave, valor in pessoa.items():
    print(chave, valor)
```

# Iteração

Dicionários são iteráveis.

Ao iterar diretamente, são percorridas as ==chaves==:

```python
for chave in pessoa:
    print(chave)
```

Para percorrer os valores:

```python
for valor in pessoa.values():
    print(valor)
```

Para percorrer chaves e valores:

```python
for chave, valor in pessoa.items():
    print(chave, valor)
```

# Dictionary Comprehension

Forma compacta de criar dicionários a partir de uma expressão e, opcionalmente, uma condição.

```python
quadrados = {x: x ** 2 for x in range(5)}
```

Resultado:

```python
{
    0: 0,
    1: 1,
    2: 4,
    3: 9,
    4: 16
}
```

Com condição:

```python
pares = {
    x: x ** 2
    for x in range(10)
    if x % 2 == 0
}
```

# Operações com dicionários

### União

O operador `|` combina dois dicionários:

```python
a = {"nome": "João"}
b = {"idade": 25}

c = a | b
# {"nome": "João", "idade": 25}
```

Caso existam chaves iguais, o valor do ==dicionário da direita prevalece:

```python
a = {"nome": "João"}
b = {"nome": "Maria"}

c = a | b
# {"nome": "Maria"}
```

### Atualização

O operador `|=` atualiza o próprio dicionário:

```python
a = {"nome": "João"}

a |= {"idade": 25}
# {"nome": "João", "idade": 25}
```

### Comparação

Dicionários podem ser comparados por igualdade:

```python
{"a": 1} == {"a": 1}  # True
{"a": 1} == {"a": 2}  # False
```

A ordem dos elementos não importa para a igualdade:

```python
{"a": 1, "b": 2} == {"b": 2, "a": 1}
# True
```

Dicionários não suportam comparações de ordem como `<` ou `>`.

# Cópia

Cuidado ao atribuir um dicionário a outra variável:

```python
a = {"nome": "João"}
b = a
```

Nesse caso, `a` e `b` referenciam o ==mesmo dicionário==.

Para criar uma cópia:

```python
b = a.copy()
```

ou:

```python
b = dict(a)
```

Essas formas criam uma ==cópia superficial==.

Para estruturas aninhadas, pode ser necessário `copy.deepcopy()`.

# Dicionários aninhados

Um dicionário pode conter outros dicionários:

```python
pessoas = {
    "joao": {
        "idade": 25,
        "cidade": "São Paulo"
    },
    "maria": {
        "idade": 30,
        "cidade": "Rio de Janeiro"
    }
}
```

Acesso:

```python
pessoas["joao"]["idade"]
# 25
```

Também é possível combinar dicionários com listas e outras estruturas:

```python
dados = {
    "nome": "João",
    "notas": [8, 9, 10],
    "endereco": {
        "cidade": "São Paulo",
        "cep": "00000-000"
    }
}
```

Acesso:

```python
dados["notas"][0]
# 8

dados["endereco"]["cidade"]
# "São Paulo"
```