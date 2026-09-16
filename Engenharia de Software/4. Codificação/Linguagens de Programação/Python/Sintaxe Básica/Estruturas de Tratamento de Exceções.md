---
Fonte: Autoria Própria Rea
---
# Estruturas de Tratamento de Exceções em Python
Em Python, o tratamento de exceções é feito principalmente com a estrutura ==try==. Ela permite *executar um trecho de código que pode gerar uma exceção e definir o que fazer caso isso aconteça*.

As estruturas principais são:
- `try`
- `except`
- `else`
- `finally`
- `raise`
- `assert`

Além disso, existem recursos complementares importantes, como **exceções personalizadas**, `Exception` e encadeamento de exceções.

---
## 1. try
Define o bloco de código que será ==monitorado quanto à ocorrência de exceções==.
```python
try:
    resultado = 10 / 0
```

Se uma exceção ocorrer dentro do **try**, Python procura um `except` compatível.

`try` normalmente não é utilizado sozinho para tratamento de exceções; ele precisa estar associado a pelo menos `except` ou `finally`.


## 2. except
Define ==como tratar uma exceção==.
```python
try:
    resultado = 10 / 0

except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

Aqui:
1. Python executa o `try`.
2. Ocorre `ZeroDivisionError`.
3. Python procura um `except` compatível.
4. O código do `except` é executado.

Cada `except` pode tratar um tipo diferente de exceção.


## 3. except sem especificar a exceção
É possível capturar praticamente qualquer exceção:
```python
try:
    codigo_perigoso()

except:
    print("Alguma exceção ocorreu.")
```

Porém, **isso geralmente deve ser evitado**.

É preferível:
```python
except Exception:
    print("Alguma exceção ocorreu.")
```

E, melhor ainda, capturar especificamente aquilo que você espera:
```python
except ValueError:
    ...
```

Isso evita esconder erros que deveriam continuar sendo identificados.


## 4. Acessando a exceção
Podemos armazenar a exceção em uma variável usando `as`.
```python
try:
    numero = int("abc")

except ValueError as erro:
    print(erro)
```

Saída:
```text
invalid literal for int() with base 10: 'abc'
```

Isso é útil para obter informações sobre o erro.


## 5. `else`
O else é executado ==somente se nenhuma exceção ocorrer no try==.
```python
try:
    numero = int(input("Número: "))

except ValueError:
    print("Valor inválido.")

else:
    print(f"Você digitou {numero}.")
```

Podemos pensar assim:
```text
try
 │
 ├── exceção → except
 │
 └── sem exceção → else
```


## 6. `finally`
O finally é executado ==independentemente de ocorrer ou não uma exceção==.
```python
try:
    arquivo = open("dados.txt")
    conteudo = arquivo.read()

except FileNotFoundError:
    print("Arquivo não encontrado.")

finally:
    print("Finalizando operação.")
```

Fluxo:
```text
              ┌─ exceção ─────→ except ─┐
try ──────────┤                          ├→ finally
              └─ sem exceção → else ────┘
```

O *finally* é especialmente útil para **limpeza de recursos**:
```python
arquivo = open("dados.txt")

try:
    conteudo = arquivo.read()

finally:
    arquivo.close()
```

Mesmo que `read()` gere uma exceção, `arquivo.close()` será executado.


## 7. raise
Enquanto try/except serve principalmente para tratar exceçõe, raise serve para ==provocar uma exceção deliberadamente==.
```python
idade = -10

if idade < 0:
    raise ValueError("A idade não pode ser negativa.")
```

O programa gera:
```text
ValueError: A idade não pode ser negativa.
```


## 8. `raise` dentro de `except`
Também podemos capturar uma exceção e depois lançá-la novamente.
```python
try:
    numero = int("abc")

except ValueError:
    print("Erro ao converter o número.")
    raise
```

O *raise* sem argumento **relança a exceção atual**.

Isso é chamado de `re-raising`.

É útil quando queremos registrar ou tratar parcialmente um erro, mas ainda permitir que ele continue subindo pela cadeia de chamadas.


## 9. `assert`
Verifica uma condição que esperamos que seja verdadeira.
```python
idade = 20

assert idade >= 18
```

Se a condição for falsa:
```python
idade = 15

assert idade >= 18
```

Python gera:
```text
AssertionError
```

Também podemos fornecer uma mensagem:
```python
assert idade >= 18, "Usuário precisa ser maior de idade."
```

### Quando usar?
Principalmente para ==verificar invariantes e condições que deveriam ser verdadeiras durante o desenvolvimento.

Não é recomendado utilizar *assert* para validações normais de entrada do usuário, porque as asserções podem ser desativadas quando Python é executado com otimização.

Para validação normal:
```python
if idade < 18:
    raise ValueError("Idade inválida.")
```


## 10. Exceções personalizadas
Podemos criar nossas próprias exceções herdando de ==Exception==.
```python
class SaldoInsuficienteError(Exception):
    pass
```

Depois:
```python
saldo = 100
valor = 200

if valor > saldo:
    raise SaldoInsuficienteError("Saldo insuficiente.")
```

E podemos tratá-la:
```python
try:
    sacar(200)

except SaldoInsuficienteError:
    print("Não foi possível realizar o saque.")
```

Isso permite criar uma hierarquia de erros específica para o domínio da aplicação.


## 11. Hierarquia de exceções
As exceções possuem uma hierarquia de classes.

Por exemplo:
```text
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ValueError
    ├── TypeError
    ├── RuntimeError
    ├── OSError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    └── ...
```

Por isso:
```python
except Exception:
```

consegue capturar:
```python
ValueError
TypeError
KeyError
IndexError
...
```

Mas não captura diretamente exceções como ==KeyboardInterrupt==, que estão fora de *Exception*.

Na prática, Exception é a classe-base normalmente utilizada para capturar erros de execução da aplicação.


## 12. Capturando várias exceções em um único `except`
Podemos agrupar tipos de exceção:
```python
try:
    numero = int(input())
    resultado = 10 / numero

except (ValueError, ZeroDivisionError):
    print("Entrada inválida.")
```

É equivalente a dizer:
```text
se ocorrer ValueError OU ZeroDivisionError
→ execute este tratamento
```


## 13. Ordem dos `except`
A ordem importa.

Errado:
```python
try:
    ...

except Exception:
    ...

except ValueError:
    ...
```
`ValueError` nunca será alcançado, porque `Exception` já captura `ValueError`.

Correto:
```python
try:
    ...

except ValueError:
    ...

except Exception:
    ...
```

A regra é:
> **Exceções mais específicas devem vir antes das mais genéricas.**


## 14. Exceções aninhadas
Um `try` pode estar dentro de outro `try`.

```python
try:
    try:
        numero = int(input())

    except ValueError:
        print("Número inválido.")

except Exception:
    print("Outro erro ocorreu.")
```

Isso é permitido, mas deve ser utilizado apenas quando existe uma necessidade real de separar níveis de tratamento.


## 15. Encadeamento de exceções
Python permite indicar que uma exceção foi causada por outra.
```python
try:
    numero = int("abc")

except ValueError as erro:
    raise RuntimeError("Falha ao processar o número.") from erro
```

Isso cria uma relação:
```text
RuntimeError
    ↑
causada por
    ↑
ValueError
```

É particularmente útil quando queremos **traduzir uma exceção de baixo nível para uma exceção mais significativa para determinada camada da aplicação**.


## 16. `raise ... from None`
Podemos ocultar o encadeamento explícito:
```python
try:
    numero = int("abc")

except ValueError:
    raise RuntimeError("Número inválido.") from None
```

Nesse caso, a causa original não aparece no traceback como exceção encadeada.


## 17. Context Manager: `with`
with não é propriamente uma estrutura de tratamento de exceções, mas está diretamente relacionado ao gerenciamento seguro de recursos.

Por exemplo, em vez de:
```python
arquivo = open("dados.txt")

try:
    conteudo = arquivo.read()

finally:
    arquivo.close()
```

podemos utilizar:
```python
with open("dados.txt") as arquivo:
    conteudo = arquivo.read()
```

O `with` utiliza o **protocolo de gerenciamento de contexto** (`__enter__` / `__exit__`) para garantir a liberação do recurso.

É uma alternativa mais idiomática para muitos casos em que anteriormente utilizaríamos `try/finally`.
