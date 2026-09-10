---
Fonte: Autoria Própria Rea
---
# Comparação entre as estruturas

| Estrutura    | Ordenada | Mutável | Indexada | Duplicados               | Acesso principal | Uso típico                                   |
| ------------ | -------- | ------- | -------- | ------------------------ | ---------------- | -------------------------------------------- |
| *Lista*      | Sim      | Sim     | Sim      | Permite                  | Índice           | Coleção ordenada que precisa ser modificada  |
| *Tupla*      | Sim      | Não     | Sim      | Permite                  | Índice           | Coleção ordenada que não deve ser modificada |
| *Conjunto*   | Não      | Sim     | Não      | **Não permite**          | Elemento         | Elementos únicos e operações de conjuntos    |
| *Dicionário* | Sim*     | Sim     | Não      | Chaves não podem repetir | Chave            | Associação entre chaves e valores            |

* Dicionários preservam a **ordem de inserção** desde Python 3.7, mas não são estruturas indexadas como listas e tuplas.

## Quando usar cada um

**Lista** → use quando você precisa de uma coleção *ordenada e modificável*, especialmente quando os elementos podem ser adicionados, removidos ou alterados.

**Tupla** → use quando você precisa de uma coleção *ordenada que não deve ser modificada*. Também é comum para representar conjuntos fixos de valores, como coordenadas ou registros simples.

**Conjunto** → use quando a *unicidade dos elementos* é importante ou quando você precisa realizar operações como união, interseção e diferença. Não use quando precisar depender da ordem ou de índices.

**Dicionário** → use quando os dados possuem uma relação de *chave → valor* e você quer localizar valores por uma chave, em vez de por posição.

### Regra prática

```text
Preciso de uma sequência modificável?   → list
Preciso de uma sequência imutável?      → tuple
Preciso de elementos únicos?            → set
Preciso relacionar chave → valor?       → dict
```

Uma distinção importante é que ==listas e tuplas são orientadas à posição==, enquanto *dicionários são orientados à chave* e **conjuntos são orientados à unicidade dos elementos**.