# bin/ (Estrutura Física)

- Pasta ==gerada automaticamente== dentro de cada projeto, criada pelo build.
- Guarda o ==resultado final da compilação==: o que de fato é executado ou distribuído.
- Existe ==uma `bin/` por projeto==, não uma para a solution inteira.
- O nome vem de _binaries_ (binários).

## Estrutura
```
Loja.Api/
└── bin/
    ├── Debug/
    │   └── net8.0/          <- resultado do build em Debug
    └── Release/
        └── net8.0/          <- resultado do build em Release
            └── publish/     <- resultado do dotnet publish
```

O caminho segue o padrão `bin/<Configuração>/<TargetFramework>/`.

## O que fica dentro

|Arquivo|Papel|
|---|---|
|`Loja.Api.dll`|Código compilado do projeto (em IL)|
|`Loja.Api.exe`|Executável de inicialização (aplicações, no Windows)|
|`Loja.Api.pdb`|Símbolos de depuração: ligam o código compilado às linhas do `.cs`|
|`Loja.Api.deps.json`|Lista de dependências da aplicação|
|`Loja.Api.runtimeconfig.json`|Configuração de execução (versão do runtime .NET)|
|`.dll` de terceiros|Pacotes NuGet e projetos referenciados, copiados para cá|

Em projetos que ==referenciam outros==, os `.dll` dos referenciados também são copiados para a `bin/` de quem os consome.

## Por que existe a separação por configuração
- `Debug` e `Release` geram saídas diferentes (com ou sem otimização e símbolos).
- Como cada uma fica em sua subpasta, ==uma não sobrescreve a outra==.

## bin/ x obj/

| Pasta  | Conteúdo                                                 |
| ------ | -------------------------------------------------------- |
| `obj/` | Arquivos **intermediários**, usados durante a compilação |
| `bin/` | **Produto final**, o que você executa                    |

## Pontos de atenção
- **Não se edita** nada aqui: qualquer alteração é sobrescrita no próximo build.
- **Pode ser apagada** a qualquer momento (`dotnet clean` ou manualmente), pois é recriada no build seguinte.
- **Não vai para o Git**: entra no `.gitignore`.
- Para executar a aplicação, o `dotnet run` usa essa saída por trás; para distribuir, o correto é o `dotnet publish`, não copiar a `bin/` inteira.
- Erros do tipo "arquivo em uso" ao compilar costumam vir de uma instância da aplicação ainda rodando e travando os arquivos da `bin/`.
