---
Fonte: Professor Nelio
Fonte 2: Autoria Própria Rea
---
# Solution (Estrutura Física)

- Fisicamente, a solution é a ==pasta raiz== do sistema no disco.
- Dentro dela ficam o arquivo de solution e as ==pastas dos projetos==.
- É o ponto de partida: tudo o que pertence ao sistema está abaixo dessa pasta.

```
Loja/                      <- pasta raiz da solution
├── Loja.sln               <- arquivo da solution
├── .gitignore
├── README.md
├── src/
│   ├── Loja.Api/          <- pasta de um projeto
│   └── Loja.Domain/       <- pasta de outro projeto
└── tests/
    └── Loja.Tests/
```

## Convenções
- ==Uma pasta por projeto==, com o mesmo nome do projeto (`Loja.Api/`).
- Separar em `src/` (código da aplicação) e `tests/` (testes) é comum, mas opcional.
- Na raiz ficam arquivos que valem para o sistema todo: `.gitignore`, `README.md`, configurações compartilhadas.
- A raiz é também o ==repositório Git==: um repositório por solution é o padrão.

## Criando pela CLI
```bash
mkdir Loja
cd Loja
dotnet new sln -n Loja
```

Isso cria a pasta raiz já com o arquivo de solution. Os projetos são adicionados depois.

## Pontos de atenção
- A pasta da solution ==não guarda código diretamente==: o código fica nas pastas dos projetos.
- Não é obrigatório que os projetos estejam dentro da pasta da solution, mas é a prática padrão.
- Se você mover a pasta raiz inteira, a estrutura interna se mantém.