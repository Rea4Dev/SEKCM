---
Fonte: Professor Nelio
Fonte 2: Autoria Própria Rea
---
# Organização Lógica

Como o código é ==agrupado conceitualmente==, do mais amplo ao mais específico:

```
Solution
└── Project
    └── Namespaces
        └── Classes
```

## Solution
- Representa o ==sistema como um todo==.
- Agrupa os projetos que trabalham juntos para entregar uma mesma aplicação.
- Exemplo: a solution `Loja` reúne tudo o que faz a loja funcionar.

## Project
- Parte do sistema com ==responsabilidade própria==.
- Pode ser uma aplicação executável ou uma biblioteca reutilizável.
- Projetos podem *depender de outros* (o projeto A usa o código do projeto B).
- Exemplo: `Loja.Api`, `Loja.Domain`, `Loja.Tests`.

## Namespaces
- Agrupam tipos (classes, interfaces, enums) ==por assunto==.
- Servem para *organizar* e para *evitar conflito de nomes* (duas classes `Produto` em contextos diferentes).
- Convenção: `Projeto.Assunto`, por exemplo `Loja.Domain.Produtos`.
- Para usar tipos de outro namespace, importa-se com `using`.

```csharp
namespace Loja.Domain.Produtos;

public class Produto { }
```

```csharp
using Loja.Domain.Produtos;
```

## Classes
- Menor unidade de organização: um ==molde== que define dados (propriedades) e comportamento (métodos).
- Ficam sempre dentro de um namespace.

```csharp
namespace Loja.Domain.Produtos;

public class Produto
{
    public string Nome { get; set; }
    public decimal Preco { get; set; }

    public void AplicarDesconto(decimal percentual)
    {
        Preco -= Preco * percentual / 100;
    }
}
```