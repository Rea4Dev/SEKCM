---
Fonte: Autoria Própria Rea
---
# Estruturas de Interrupção e Desvio em Python

São estruturas que ==alteram o fluxo normal de execução== de um programa, permitindo interromper, pular ou redirecionar a execução de blocos de código.


## 1. break
Interrompe imediatamente o laço de repetição (for ou while) ==mais interno==.
```python
for numero in range(5):
    if numero == 2:
        break

    print(numero)
```

**Saída:**
```text
0
1
```

> `break` encerra apenas o laço em que está inserido.


## 2. continue
Interrompe apenas a iteração atual e passa para a próxima iteração do laço.
```python
for numero in range(5):
    if numero == 2:
        continue

    print(numero)
```

**Saída:**
```text
0
1
3
4
```

> `continue` não encerra o laço.


## 3. pass
Não desvia efetivamente o fluxo. É uma instrução nula, utilizada quando a sintaxe exige um bloco de código, mas nenhuma ação deve ser executada.
```python
if idade >= 18:
    pass
else:
    print("Menor de idade")
```

Também é comum em estruturas ainda não implementadas:
```python
def calcular():
    pass
```

> `pass` pode ser entendido como "não faça nada".


## 4. return
Encerra a execução de uma função e, opcionalmente, retorna um valor para quem a chamou.
```python
def somar(a, b):
    return a + b

resultado = somar(2, 3)
```

Também pode ser usado para interromper a função antecipadamente:
```python
def verificar(idade):
    if idade < 18:
        return

    print("Acesso permitido")
```

> Diferentemente de `break`, `return` não está limitado a estruturas de repetição: ele encerra a **função inteira**.


## 5. yield
Interrompe temporariamente a execução de uma função geradora, produzindo um valor. A execução pode continuar posteriormente a partir daquele ponto.
```python
def numeros():
    yield 1
    yield 2
    yield 3

for i in numeros():
    print(i)
```


Cada `yield` pausa a função e entrega um valor ao consumidor.

> Diferentemente de `return`, `yield` **não encerra definitivamente** a função.