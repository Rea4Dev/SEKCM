# obj/ (Estrutura Física)

- Pasta ==gerada automaticamente== dentro de cada projeto, criada pelo restore e pelo build.
- Guarda os ==arquivos intermediários==: o que o build produz e usa no meio do caminho, antes do resultado final ir para a `bin/`.
- Existe ==uma `obj/` por projeto==.
- O nome vem de _objects_ (objetos intermediários de compilação).

## Estrutura
```
Loja.Api/
└── obj/
    ├── project.assets.json          <- resultado do restore
    ├── project.nuget.cache
    ├── Loja.Api.csproj.nuget.g.props
    ├── Loja.Api.csproj.nuget.g.targets
    └── Debug/
        └── net8.0/                  <- intermediários da compilação
            ├── Loja.Api.dll
            ├── Loja.Api.pdb
            ├── Loja.Api.AssemblyInfo.cs
            └── Loja.Api.GlobalUsings.g.cs
```

## O que fica dentro

| Arquivo                                 | Papel                                                                            |
| --------------------------------------- | -------------------------------------------------------------------------------- |
| `project.assets.json`                   | Mapa completo das dependências resolvidas no **restore** (pacotes e referências) |
| `*.nuget.g.props` / `*.nuget.g.targets` | Configurações geradas a partir dos pacotes NuGet, importadas no build            |
| `project.nuget.cache`                   | Permite pular o restore quando nada mudou                                        |
| `*.AssemblyInfo.cs`                     | Código **gerado**: metadados do assembly (nome, versão)                          |
| `*.GlobalUsings.g.cs`                   | Código **gerado** com os `using` implícitos (`ImplicitUsings`)                   |
| `.dll` e `.pdb` intermediários          | Saída da compilação, antes de ser copiada para a `bin/`                          |
| arquivos `.cache`                       | Controle do **build incremental** (o que mudou desde a última vez)               |

Os arquivos com `.g.` no nome são **gerados** (_generated_): você não escreve nem edita.

## Papel no fluxo do build
```
Restore  -> grava project.assets.json na obj/
Compile  -> gera arquivos e .dll intermediário na obj/Debug/...
Saída    -> copia o resultado final para a bin/
```

## obj/ x bin/

| Pasta  | Conteúdo                           | Quem usa          |
| ------ | ---------------------------------- | ----------------- |
| `obj/` | Intermediários e controle do build | O próprio build   |
| `bin/` | Produto final                      | Você e a execução |

## Pontos de atenção
- **Não se edita** nada aqui: tudo é regenerado.
- **Não vai para o Git**: entra no `.gitignore`.
- **Pode ser apagada** a qualquer momento (`dotnet clean` ou manualmente), pois o restore e o build a recriam.
- Se o build apresentar erros estranhos de dependência ou cache, ==apagar `bin/` e `obj/`== e rodar `dotnet build` de novo é a solução clássica.
- Editores e a IDE leem a `obj/` (principalmente `project.assets.json`) para saber quais pacotes o projeto usa, por isso ela precisa existir para o IntelliSense funcionar direito.
