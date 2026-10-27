# Build (Estrutura Física)

- Processo que ==transforma o código-fonte (`.cs`) em um artefato executável==: `.dll` (biblioteca) ou `.exe` (aplicação).
- É guiado pelo `.csproj` de cada projeto e orquestrado pela solution.
- Feito pelo ==.NET SDK==, usando o compilador *Roslyn*.

## Fluxo do build
```
.cs + .csproj
      │
      ▼
1. Restore   -> baixa pacotes NuGet e resolve referências
      │
      ▼
2. Compile   -> Roslyn compila os .cs em IL (linguagem intermediária)
      │
      ▼
3. Saída     -> gera .dll / .exe em bin/
```

- **IL (Intermediate Language):** o C# não vira código de máquina direto. Vira um formato intermediário, que o runtime do .NET converte em código nativo na hora da execução (JIT).

## Comandos da CLI
```bash
dotnet restore     # só restaura dependências
dotnet build       # restore + compilação
dotnet run         # build + executa o projeto
dotnet clean       # apaga a saída gerada
dotnet publish     # gera a versão final para distribuição
```

- O `dotnet build` já executa o restore automaticamente.
- Rodando na pasta da solution, compila ==todos os projetos==, na ==ordem das dependências==.

## Onde fica o resultado
```
Loja.Api/
├── obj/                        <- arquivos intermediários
└── bin/
    └── Debug/
        └── net8.0/
            ├── Loja.Api.dll            <- código compilado
            ├── Loja.Api.exe            <- executável (aplicações)
            ├── Loja.Api.pdb            <- símbolos de depuração
            ├── Loja.Api.deps.json      <- lista de dependências
            └── Loja.Api.runtimeconfig.json  <- configuração de execução
```

## Configurações: Debug e Release

| Configuração     | Uso                                                                |
| ---------------- | ------------------------------------------------------------------ |
| `Debug` (padrão) | Desenvolvimento: inclui símbolos, sem otimização, facilita depurar |
| `Release`        | Produção: código otimizado, mais rápido e enxuto                   |

```bash
dotnet build -c Release
```

A saída vai para `bin/Release/net8.0/`.

## Build x Publish
- **Build:** gera a saída para desenvolvimento e teste local.
- **Publish:** gera o **pacote final**, com tudo o que a aplicação precisa para ser implantada, na pasta `bin/Release/net8.0/publish/`.

## Pontos de atenção
- O build é **incremental**: só recompila o que mudou.
- Se algo estranho acontecer, `dotnet clean` seguido de `dotnet build` resolve boa parte dos casos.
- Erros de compilação **interrompem** o build e nenhum artefato novo é gerado.
- `bin/` e `obj/` são recriadas a cada build e ficam fora do Git.
