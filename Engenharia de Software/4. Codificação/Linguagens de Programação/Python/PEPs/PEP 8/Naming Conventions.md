---
Fonte: Autoria Própria Rea
---
# Naming Conventions

Ao codificar, constantemente o desenvolvedor estará atribuindo nome aos elementos de código. Por motivos de organização, padronização e clareza, as linguagens de programação adotam padrões de nomeação para as variáveis, constantes, funções, classes etc.

Entretanto, este padrão não é universal para as linguagens, ou seja, cada linguagem de programação adota uma convenção de nomeação. 

## Em Python
A convenção adotada é o ==PEP 8== (o guia de estilo oficial da linguagem, veja <a href="https://peps.python.org/pep-0008/">aqui</a>), que recomenda principalmente o uso do *snake_case*, palavras separadas por underscore (`_`) e escritas em `minúsculas`.

Segue uma tabela resumindo as convenções recomendadas para cada elemento de código em Python:

| Elemento                        | Convenção                                    | Exemplo                               |
| ------------------------------- | -------------------------------------------- | ------------------------------------- |
| *Variáveis*                     | snake_case                                   | `idade_maxima`                        |
| *Funções*                       | snake_case                                   | `calcular_media()`,                   |
| *Métodos*                       | snake_case                                   | `def obter_saldo(self):`              |
| *Módulos*                       | snake_case (nomes curtos e minúsculos)       | `utils.py`, `gerenciador_arquivos.py` |
| Classes                         | PascalCase                                   | `class ContaBancaria:`                |
| Constantes                      | UPPER_CASE (com underscore)                  | `TAXA_JUROS = 0.05`                   |
| Pacotes                         | minúsculas, sem underscore preferencialmente | `pacoteexemplo`, `meupacote`          |
| Atributos "privados"            | underscore no início                         | `_saldo`, `_senha`                    |
| Atributos "fortemente privados" | dois underscores no início (name mangling)   | `__token`, `__chave_secreta`          |
| Métodos mágicos/dunder          | dois underscores antes e depois              | `__init__`, `__str__`, `__len__`      |
