---
Fonte 1 (reorganizada e grifada): https://docs.python.org/pt-br/3.14/tutorial/controlflow.html#match-statements
Fonte 2: Autoria Própria Rea
Nota: Conteúdo expansível. Há mais na documentação oficial e há uma PEP voltada a isso. Por hora, priorizei praticidade.
---
# Match Case

>[!Note] Documentação Oficial
>Uma instrução [`match`](https://docs.python.org/pt-br/3.14/reference/compound_stmts.html#match) pega uma expressão e compara seu valor com padrões sucessivos fornecidos como um ou mais blocos de case.
>
>Isso é superficialmente semelhante a uma instrução switch em C, Java ou JavaScript (e muitas outras linguagens), mas muito mais parecido com a correspondência de padrões em linguages como Rust ou Haskell.
>
>==Apenas o primeiro padrão que corresponder será executado==, podendo também extrair componentes (elementos de sequência ou atributos de objetos) do valor para variáveis.
>
>*Se nenhum caso corresponder, nenhuma das ramificações será executada*.
>
>A forma mais simples compara um valor de assunto com um ou mais literais:
```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```
>[!Note] Continuação de Documentação Oficial
>Observe o último bloco: o “nome da variável” `_` atua como um _curinga_ e nunca falha em corresponder.
>
>Você pode combinar vários literais em um único padrão usando `|` (“ou”):
```python
case 401 | 403 | 404:
    return "Não permitido"
```

## Desempacotador
Os padrões podem separar valores e atribuí-los a variáveis:

```python
comando = ("cadastrar", "João")

match comando:
    case ("cadastrar", nome):
        print(f"Cadastrando {nome}")

    case ("remover", nome):
        print(f"Removendo {nome}")

    case ("listar",):
        print("Listando usuários")

    case _:
        print("Comando desconhecido")
```