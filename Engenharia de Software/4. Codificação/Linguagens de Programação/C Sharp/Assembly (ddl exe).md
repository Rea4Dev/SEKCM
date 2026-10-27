# Assembly (.dll / .exe)

Agrupamento *físico* de classes relacionadas (build). Também chamado "project".

Em tenho um sistema enorme e vou dividir em subsistemas.
- Desta forma, separei tudo que fosse relacionado a financeiro no Assembly "Financeiro".
- Da mesma forma, separei e agrupei tudo que fosse relacionado a gráficos em um subprojeto "Gráficos".

E dentro de cada Assembly, podemos separar em namespaces e classes...

![[Pasted image 20260927205114.png]]

`.dll` _Dynamic Link Library_
- ==Assembly== é a unidade compilada do .NET: o ==artefato que o build produz== a partir de um projeto.
- Regra geral: ==1 projeto = 1 assembly==.
- Fisicamente, é um arquivo `.dll` ou `.exe`.
- É a menor unidade de ==distribuição, versionamento e reuso== no .NET.

## .dll x .exe

| Tipo   | Origem                | Característica                                             |
| ------ | --------------------- | ---------------------------------------------------------- |
| `.dll` | Biblioteca de classes | Sem ponto de entrada, ==usada por outros== assemblies      |
| `.exe` | Aplicação             | Tem ponto de entrada (`Program.cs`), ==pode ser iniciada== |

- Ambos são assemblies e têm o mesmo formato interno.
- No .NET moderno, o `.exe` é só um **lançador** (_apphost_). O código da aplicação fica no `.dll` de mesmo nome, que também pode ser executado com `dotnet Loja.Api.dll`.

## O que tem dentro

|Parte|Conteúdo|
|---|---|
|**Código IL**|Instruções em linguagem intermediária, resultado da compilação dos `.cs`|
|**Metadados**|Descrição de todos os tipos: classes, métodos, propriedades, parâmetros|
|**Manifesto**|Identidade do assembly e lista de outros assemblies de que ele depende|
|**Recursos** (opcional)|Imagens, textos e outros arquivos embutidos|

Os metadados permitem que o assembly seja **autodescritivo**: qualquer ferramenta consegue ler o que ele contém sem precisar do código-fonte.

## Identidade
Todo assembly se identifica por:

- **Nome** (`Loja.Api`)
- **Versão** (`1.0.0.0`)
- **Cultura** (idioma, quando aplicável)
- **Chave pública** (opcional, para assemblies com nome forte)

Esses dados vêm do `.csproj` e ficam registrados no manifesto.

## Como é usado
- **Referência entre projetos:** quando `Loja.Api` referencia `Loja.Domain`, o build copia o `Loja.Domain.dll` para a `bin/` de `Loja.Api`.
- **Execução:** o **CLR** (runtime do .NET) carrega o assembly, e o compilador **JIT** converte o IL em código de máquina na hora, conforme o código é executado.
- **Pacotes NuGet:** cada pacote entrega um ou mais `.dll` que o projeto passa a referenciar.

```
.cs  --(Roslyn)-->  Assembly (IL + metadados)  --(CLR/JIT)-->  código nativo
```

## Assembly x Namespace

|Conceito|Natureza|Função|
|---|---|---|
|**Assembly**|Física (arquivo)|Pacote de código compilado|
|**Namespace**|Lógica (rótulo)|Organiza tipos por assunto|

- Um assembly pode conter ==vários namespaces==.
- Um namespace pode se ==espalhar por vários assemblies==.

## Pontos de atenção
- Um assembly pode ser inspecionado sem o código-fonte, com ferramentas como **ILSpy** ou **dotnet-ildasm**, justamente por conter IL e metadados.
- Em C#, `Assembly` também é uma classe (`System.Reflection.Assembly`), usada em **reflexão** para ler assemblies em tempo de execução. É um assunto para mais adiante.
- `.dll` gerado por C# não é o mesmo que uma DLL nativa de C/C++: só roda sob o runtime do .NET.
- O assembly final vai para a `bin/`, mas uma versão intermediária também aparece na `obj/`.