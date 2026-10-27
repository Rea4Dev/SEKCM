# Project (Organização Lógica)

- Parte do sistema com ==responsabilidade própria e bem definida==.
- Unidade lógica dentro da solution: cada projeto responde a uma pergunta como "o que essa parte do sistema faz?".
- Dentro dele ficam os *namespaces e classes* que cumprem essa responsabilidade.
- Regra geral: **1 projeto = 1 assembly** (a parte física fica no outro arquivo).

## Por que dividir em projetos
- `Separação de responsabilidades`: cada parte cuida de um assunto.
- `Reuso`: uma biblioteca pode ser usada por vários projetos.
- `Isolamento`: um projeto só enxerga o que referencia, o que impede dependências indevidas.
- `Manutenção e testes`: mudanças e testes ficam localizados.
- `Trabalho em equipe`: partes diferentes evoluem com menos conflito.

## Tipos lógicos de projeto

| Tipo                      | Papel                                       | Exemplo                    |
| ------------------------- | ------------------------------------------- | -------------------------- |
| **Aplicação**             | Tem ponto de entrada, ==inicia a execução== | `Loja.Api`, `Loja.Console` |
| **Biblioteca de classes** | Reúne código para ser ==usado por outros==  | `Loja.Domain`, `Loja.Data` |
| **Testes**                | Verifica o comportamento dos demais         | `Loja.Tests`               |

## Divisão típica por responsabilidade

```
Loja.Api      -> entrada: recebe requisições e devolve respostas
Loja.Domain   -> núcleo: entidades e regras de negócio
Loja.Data     -> acesso a dados: banco, repositórios
Loja.Tests    -> testes automatizados
```

## Dependências entre projetos
- Um projeto usa outro por ==referência==: A referencia B significa que A enxerga o código público de B.
- A dependência tem *direção única*:

```
Api ──> Domain <── Data
 └────> Data
Tests ──> (Api, Domain, Data)
```

- **Não pode haver referência circular** (A usa B e B usa A): o build recusa.
- Boa prática: o projeto central (`Domain`) **não depende de ninguém**, e os demais dependem dele.

## Visibilidade entre projetos
- Um projeto só expõe para fora o que for `public`.
- O que é `internal` fica visível ==apenas dentro do próprio projeto==.
- Por isso o projeto funciona como uma **fronteira de encapsulamento**.

## Convenções de nome
- Formato `Solution.Responsabilidade`: `Loja.Domain`, `Loja.Api`.
- O nome do projeto costuma ser também o ==namespace raiz== dele (`Loja.Domain`), e os namespaces internos derivam dele (`Loja.Domain.Produtos`).

## Pontos de atenção
- Não existe número certo de projetos: para estudo ou sistemas pequenos, ==um projeto basta==. Dividir sem necessidade só adiciona complexidade.
- Dividir faz sentido quando há *responsabilidades distintas* ou **reuso** real.
- Projeto e namespace são coisas diferentes: o projeto é a fronteira de compilação e dependência, o namespace é só rótulo de organização.