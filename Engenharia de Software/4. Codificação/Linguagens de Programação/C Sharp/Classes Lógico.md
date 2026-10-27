# Classes (Organização Lógica)

- Menor unidade de organização lógica: fica dentro de um ==namespace==, que fica dentro de um ==projeto==.
- É um ==molde== que define ==dados== (o que o objeto guarda) e ==comportamento== (o que ele faz).
- Cada classe deve ter ==uma responsabilidade clara==.

## Classe x Objeto
- `Classe`: a definição, o molde.
- `Objeto (instância)`: o exemplar criado a partir do molde, com `new`.

```csharp
var p1 = new Produto();   // objeto
var p2 = new Produto();   // outro objeto, independente do primeiro
```

## Anatomia
```csharp
namespace Loja.Domain.Produtos;

public class Produto
{
    private decimal _preco;                    // campo

    public string Nome { get; set; }           // propriedade

    public Produto(string nome)                // construtor
    {
        Nome = nome;
    }

    public void AplicarDesconto(decimal pct)   // método
    {
        _preco -= _preco * pct / 100;
    }
}
```

## Membros de uma classe

| Membro          | Papel                                             |
| --------------- | ------------------------------------------------- |
| **Campo**       | Variável interna que guarda um dado               |
| **Propriedade** | Acesso controlado a um dado (`get` e `set`)       |
| **Construtor**  | Roda ao criar o objeto e o deixa em estado válido |
| **Método**      | Comportamento: uma ação que o objeto executa      |

## Modificadores de acesso
Definem ==quem enxerga== a classe e seus membros:

| Modificador | Visível para                                      |
| ----------- | ------------------------------------------------- |
| `public`    | Qualquer código                                   |
| `internal`  | Apenas o **mesmo projeto** (padrão para classes)  |
| `private`   | Apenas a **própria classe** (padrão para membros) |

Regra prática: **expor o mínimo necessário**. Isso é o encapsulamento.

## Outros tipos que ficam no mesmo nível
A classe é o tipo mais comum, mas convive no namespace com:

- `interface`: contrato de comportamento
- `enum`: conjunto fixo de valores
- `struct`: tipo de valor, leve
- `record`: tipo voltado a representar dados

## Convenções
- Nome em **PascalCase** e no **singular** (`Produto`, não `Produtos`).
- Nome de **substantivo**, que descreve o que a classe representa.
- Uma classe por arquivo, com o arquivo nomeado igual à classe.

## Pontos de atenção
- Classe sem modificador é `internal`: para outro projeto usá-la, ela precisa ser `public`.
- Classes muito grandes, com várias responsabilidades, são sinal de que devem ser divididas.
- `static class` não é instanciada: serve para agrupar funções utilitárias.
- Herança, polimorfismo e interfaces são assuntos próprios, para mais adiante.