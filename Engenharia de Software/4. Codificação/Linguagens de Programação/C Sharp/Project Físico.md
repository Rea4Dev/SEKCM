# Project (Estrutura Física)

- Fisicamente, o projeto é uma ==pasta== dentro da solution que reúne tudo o que compõe uma unidade compilável.
- Cada projeto gera ==um artefato== ao ser compilado: uma aplicação (`.exe`) ou uma biblioteca (`.dll`).
- A pasta tem o ==mesmo nome== do projeto (`Loja.Api/`).

## Estrutura típica no disco
```
Loja.Api/                  <- pasta do projeto
├── Loja.Api.csproj        <- definição do projeto (próximo tópico)
├── Program.cs             <- ponto de entrada (em aplicações)
├── Controllers/           <- subpasta de organização
│   └── ProdutosController.cs
├── Models/
│   └── Produto.cs
├── bin/                   <- gerada: resultado da compilação
└── obj/                   <- gerada: arquivos intermediários
```

## O que fica dentro

|Item|Papel|
|---|---|
|`.csproj`|Define como o projeto é compilado|
|Arquivos `.cs`|O código-fonte|
|Subpastas|Organização interna do código|
|`bin/` e `obj/`|Geradas pela compilação|

## Pastas geradas: `bin/` e `obj/`
- `obj/`: arquivos intermediários do processo de compilação.
- `bin/`: o **resultado final** (o `.dll` ou `.exe`), separado por configuração, por exemplo `bin/Debug/net8.0/`.
- **Não vão para o Git** (entram no `.gitignore`) e podem ser apagadas a qualquer momento, pois são recriadas no próximo build.

## Tipos de projeto (pelo resultado)
- **Aplicação:** tem ponto de entrada (`Program.cs`) e gera um executável.
- **Biblioteca de classes:** sem ponto de entrada, gera um `.dll` para ser usado por outros projetos.

## Conexão entre projetos
- Um projeto usa outro por **referência de projeto**, declarada no `.csproj` do que consome.
- Pela CLI: `dotnet add Loja.Api reference Loja.Domain`.

## Criando pela CLI
```bash
dotnet new console -n Loja.Api -o src/Loja.Api   # aplicação
dotnet new classlib -n Loja.Domain -o src/Loja.Domain   # biblioteca
dotnet sln add src/Loja.Api src/Loja.Domain      # registra na solution
```

## Pontos de atenção
- Por convenção, as **subpastas do projeto refletem os namespaces** (`Models/` vira `Loja.Api.Models`), mas isso não é obrigatório.
- Um projeto compila de forma **independente**: só enxerga o que está na sua pasta e nas suas referências.
- O código-fonte e o `.csproj` são versionados; `bin/` e `obj/` não.