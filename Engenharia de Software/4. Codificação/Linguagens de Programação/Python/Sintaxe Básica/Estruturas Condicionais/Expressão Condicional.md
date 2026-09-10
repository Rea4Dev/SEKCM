---
Fonte: https://docs.python.org/pt-br/3.14/reference/expressions.html
Fonte 2: https://peps.python.org/pep-0308/
Fonte 3: Autoria Própria Rea
---
# Expressão Condicional

> [!Note] Documentação Oficial
> Uma expressão condicional (às vezes chamada de “operador ternário”) é uma alternativa à instrução if-else. Como é uma expressão, ela retorna um valor e pode aparecer como uma subexpressão.
> 
> A expressão `x if C else y` primeiro avalia a condição, _C_ em vez de _x_. Se _C_ for verdadeiro, _x_ é avaliado e seu valor é retornado; caso contrário, _y_ será avaliado e seu valor será retornado.
>
Veja [**PEP 308**](https://peps.python.org/pep-0308/) para mais detalhes sobre expressões condicionais.

>[!Tip]
>Caso deseje consultar um pouco do contexto histórico que gerou a PEP 308 (Expressão Condicional), consulte a **Fonte 2**.

De toda forma, Expressões Condicionais são ==inline== e permitem escolher *um valor* com base em **uma condição**.

Forma mais comum:
```python
valor_se_verdadeiro if condição else valor_se_falso
```

```python
print("aprovado" if nota >= 7 else "reprovado")
```

## Condições combinadas
A condição pode utilizar os operadores lógicos:
```python
resultado = "aceito" if idade >= 18 and renda > 2000 else "recusado"
```

Também podem ser usados:
```python
and
or
not
```

## Condicionais em expressões maiores
O resultado da expressão condicional pode ser usado diretamente:
```python
total = preco * 0.9 if cliente_vip else preco
```

Ou como argumento:
```python
print("Online" if conectado else "Offline")
```
