# Estrutura Física

- Como o sistema existe ==de fato no disco==: pastas, arquivos e o resultado da compilação.
- Responde à pergunta "==onde as coisas estão== e ==o que o build gera==?".
- Complementa a Organização Lógica: a lógica agrupa o código conceitualmente, a física o materializa em arquivos.

## Lógico x Físico

| Organização Lógica                   | Estrutura Física                     |
| ------------------------------------ | ------------------------------------ |
| Solution (o sistema)                 | Pasta raiz + arquivo `.sln`          |
| Project (parte com responsabilidade) | Pasta do projeto + arquivo `.csproj` |
| Namespace e Classe                   | Arquivos `.cs`                       |
| (sem equivalente)                    | Build, `bin/`, `obj/` e Assembly     |

## Sequência
```
Solution        pasta raiz do sistema
   │
.sln            arquivo que lista os projetos
   │
Project         pasta de cada projeto
   │
.csproj         arquivo que define como compilar
   │
.cs             arquivos de código-fonte
   │
Build           compilação do código
   │
bin/ e obj/     pastas geradas pelo build
   │
Assembly        .dll / .exe, o resultado final
```

## Divisão em duas fases

| Fase           | Itens                                       | Natureza                              |
| -------------- | ------------------------------------------- | ------------------------------------- |
| **Escrita**    | Solution, `.sln`, Project, `.csproj`, `.cs` | Arquivos que **você cria e versiona** |
| **Compilação** | Build, `bin/`, `obj/`, Assembly             | Arquivos **gerados**, fora do Git     |

## Ideia central
- O que você ==escreve== vai para o Git: `.sln`, `.csproj` e `.cs`.
- O que o build ==gera== (`bin/`, `obj/`) pode ser apagado e recriado a qualquer momento.
- O caminho completo é: ==código-fonte (`.cs`) + receita (`.csproj`) → build → assembly==.
