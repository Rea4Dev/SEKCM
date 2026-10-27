# .csproj (Estrutura Física)

- Arquivo ==XML== dentro da pasta do projeto que define ==como o projeto é compilado==.
- Um `.csproj` por projeto, com o mesmo nome da pasta (`Loja.Api.csproj`).
- É a "receita" do projeto: qual versão do .NET usar, que pacotes e outros projetos ele consome.
- Não lista os arquivos `.cs`: no formato atual (SDK-style), ==todos os `.cs` da pasta são incluídos automaticamente==.

## Exemplo
```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\Loja.Domain\Loja.Domain.csproj" />
  </ItemGroup>

</Project>
```

## Elementos principais

| Elemento            | Papel                                                                                                                                         |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `Project Sdk="..."` | Define o tipo de SDK e as regras padrão de build. `Microsoft.NET.Sdk` para console e bibliotecas, `Microsoft.NET.Sdk.Web` para aplicações web |
| `PropertyGroup`     | Agrupa **propriedades** do projeto                                                                                                            |
| `ItemGroup`         | Agrupa **itens**: pacotes e referências                                                                                                       |
| `PackageReference`  | Dependência externa, vinda do **NuGet** (nome e versão)                                                                                       |
| `ProjectReference`  | Dependência de **outro projeto** da solution (caminho relativo)                                                                               |

## Propriedades mais comuns
- `OutputType`: `Exe` gera aplicação; se omitido, gera biblioteca (`.dll`).
- `TargetFramework`: versão do .NET alvo (`net8.0`).
- `Nullable`: ativa a análise de valores nulos.
- `ImplicitUsings`: inclui automaticamente os `using` mais comuns.

## Comandos da CLI
```bash
dotnet add package Newtonsoft.Json                 # adiciona PackageReference
dotnet add reference ../Loja.Domain                # adiciona ProjectReference
dotnet build                                       # compila usando o .csproj
```

Os comandos editam o `.csproj` por você.

## Pontos de atenção
- Diferente do `.sln`, o `.csproj` **é editável à mão** com frequência e é legível.
- Deve ir para o **Git**.
- Como os `.cs` entram automaticamente, criar ou apagar um arquivo de código **não exige alterar** o `.csproj`.
- Se o projeto for compilado sem solution, o comando é executado direto sobre ele: `dotnet build Loja.Api.csproj`.