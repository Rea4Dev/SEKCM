# .sln (Estrutura Física)
Uma ==solução== em C# é um contêiner que agrupa um ou mais projetos, e possui um arquivo *.sln* que a representa.

É a partir deste arquivo que você abre a solução (e, com ela, todos os projetos que ela contém).

- Arquivo que representa a solution no disco, na ==pasta raiz==.
- É um arquivo ==de texto==: guarda a lista de projetos e as configurações de build.
- Não contém código. Só aponta para os projetos e descreve como compilá-los em conjunto.
- É o arquivo que você abre na IDE para carregar o sistema inteiro.

## O que ele guarda
- **Lista de projetos:** nome e caminho do `.csproj` de cada um, cada projeto com um identificador único (GUID).
- **Configurações de build:** por padrão `Debug` e `Release`.
- **Mapeamento** de qual configuração cada projeto usa em cada build.

## Exemplo simplificado
```C#
Microsoft Visual Studio Solution File, Format Version 12.00

Project("{FAE04EC0-...}") = "Loja.Api", "src\Loja.Api\Loja.Api.csproj", "{A1B2...}"
EndProject
Project("{FAE04EC0-...}") = "Loja.Domain", "src\Loja.Domain\Loja.Domain.csproj", "{C3D4...}"
EndProject

Global
    GlobalSection(SolutionConfigurationPlatforms) = preSolution
        Debug|Any CPU = Debug|Any CPU
        Release|Any CPU = Release|Any CPU
    EndGlobalSection
EndGlobal
```

Cada `Project(...)` é uma linha de projeto apontando para o respectivo `.csproj`.

## Comandos da CLI
```bash
dotnet new sln -n Loja                        # cria o arquivo
dotnet sln add src/Loja.Api/Loja.Api.csproj   # adiciona um projeto
dotnet sln list                               # lista os projetos
dotnet sln remove src/Loja.Api/Loja.Api.csproj
```

## Pontos de atenção
- Normalmente ==não se edita à mão==: a IDE e a CLI mantêm o arquivo.
- Deve ir para o ==Git==.
- Os caminhos dentro dele são ==relativos== à pasta da solution.
- Existe um formato mais novo, o `.slnx` (baseado em XML, mais legível e limpo). Versões recentes do SDK do .NET já o geram por padrão no `dotnet new sln`. O papel é o mesmo, muda só o formato do arquivo.
- Um projeto pode existir sem `.sln` (dá para compilar direto pelo `.csproj`), mas a solution facilita quando há vários.
