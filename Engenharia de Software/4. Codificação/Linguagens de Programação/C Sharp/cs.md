# .cs (Estrutura Física)

- Arquivo de ==texto== que contém o ==código-fonte== em C#.
- É a menor unidade física do projeto: o `.csproj` reúne os `.cs`, e o compilador os transforma em um `.dll` ou `.exe`.
- Fica dentro da pasta do projeto, em qualquer nível de subpasta.

## Anatomia de um arquivo
```csharp
using System;                       // 1. importações (using)

namespace Loja.Domain.Produtos;     // 2. namespace

public class Produto                // 3. tipo (classe, interface, enum...)
{
    public string Nome { get; set; }
}
```

Ordem padrão: `using`, depois `namespace`, depois o tipo.

## Convenções
- ==Um tipo por arquivo==, com o arquivo nomeado igual ao tipo: `Produto.cs` contém a classe `Produto`.
- Nome do arquivo em ==PascalCase==.
- Subpastas agrupam arquivos por assunto (`Models/`, `Services/`) e costumam refletir o namespace.
- Interfaces levam o prefixo `I` (`IProdutoRepository.cs`).

## Como entra na compilação
- No formato atual, ==todo `.cs` dentro da pasta do projeto é incluído automaticamente==.
- Criar, mover ou apagar um `.cs` não exige editar o `.csproj`.
- Arquivos em `bin/` e `obj/` são ignorados como fonte de código.

## Arquivos `.cs` com papel especial

| Arquivo            | Papel                                               |
| ------------------ | --------------------------------------------------- |
| `Program.cs`       | Ponto de entrada da aplicação                       |
| `GlobalUsings.cs`  | Centraliza `using` globais (`global using System;`) |
| Arquivos em `obj/` | Gerados pelo compilador, não se editam              |

## Ponto de entrada
Em projetos novos, o `Program.cs` pode ter apenas instruções soltas, sem classe nem `Main` visíveis (_top-level statements_):

```csharp
Console.WriteLine("Olá, mundo!");
```

O compilador cria a estrutura por trás.

## Criando pela CLI
```bash
dotnet new class -n Produto      # cria Produto.cs com uma classe
```

Ou simplesmente criar o arquivo pela IDE ou pelo explorador de arquivos.

## Pontos de atenção
- Nada obriga fisicamente uma classe por arquivo, mas é a prática padrão e facilita a navegação.
- O ==nome do arquivo não afeta a compilação==: quem vale é o nome declarado dentro do código.
- Deve ir para o ==Git==.