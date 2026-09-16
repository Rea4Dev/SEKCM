---
Fonte: Autoria Própria Rea
---
![[Pasted image 20260912211051.png]]

Diquinhas gerais de uso do Python. Feito de forma um pouco mais descontraída e freestyle, geralmente destinada aos detalhes que não cabem da topografia genérica.

---
# Formatação de Saída
É comum esquecer os ":" antes de ".2f". Então tome cuidado!

```python
valor = 0.9301823019258394293420341823869056456452

print(f"Formatado fica: {valor:.2f}")
```

```python
valor = 1953.50

print(f"Formatado fica: {valor:,.2f}")
```

---
# Extensão .pyw
Caso queira que seu arquivo python aja como um executável sem que você precise efetivamente o transformar em executável (e ter as dores que um executável carrega...), você pode inserir ".pyw" no final da extensão.

Basicamente, ".pyw" significa que o script deve ser executado pelo interpretador pythonw.exe (no Windows) em vez do python.exe comum. A diferença é simples, mas poderosa: pythonw.exe não abre uma janela de console (aquele terminal preto do DOS) para exibir a saída do programa, ou então (o que geralmente acontece) abrir o software setado como padrão para o tipo de arquivo (geralmente VSCode).

---
# Biblioteca rich
Biblioteca com diversas funcionalidadaes! Consulte <a href="https://rich.readthedocs.io/en/stable/index.html" style="color: grey;">clicando aqui</a>.
Há também esse vídeo que passa por diversos pontos: <a href="https://www.youtube.com/watch?v=4zbehnz-8QU" style="color: grey;">vídeo</a>.
## print anabolizado
Existe alguma forma melhor de nomear isso? Provavelmente. Entretanto, é exatamente nisso que "rich" transforma o print.

Veja-o fazer as cores em terminal ficar mais simples:
```python
from rich import print

print("[red]Vermelho[/red]")
```

Sem rich, seria
```python
print("\033[31mVermelho\033[0m")
```

## panel sedutor
Sério, olha que coisa linda!
![[Pasted image 20260912220503.png]]

## tabela cheirosa
Ok, to perdendo a mão nos títulos.
![[Pasted image 20260912221035.png]]

## inspect - WALL HACK PYTHON 2026 ATUALIZADO
Sério, é bizarro o quão legal e útil é isso aqui. Basicamente você vê TUDO sobre algo do Python. Exposed totalllllll
![[Pasted image 20260912221516.png]]

## traceback - queríamos saber disso antes...
É basicamente uma forma de invocar um anjo do debbug para te salvar nessa nossa amada linguagem interpretada.

Além de deixar tudo muito mais bonito e organizado, ele fala o que causou o erro e onde causou.

![[Pasted image 20260912222815.png]]

---
# Regex
Salva MUITA linha de código quando o assunto é buscar/validar padrões em texto. Em Python, quem cuida disso é o módulo nativo `re`.

## Funções mais usadas

```python
import re

texto = "Meu email é contato@teste.com e meu tel é 11987654321"

# search: acha a primeira ocorrência
re.search(r"\d+", texto)

# findall: acha TODAS as ocorrências (retorna lista)
re.findall(r"\d+", texto)

# sub: substitui o que encontrar
re.sub(r"\d+", "***", texto)

# match: só verifica o INÍCIO da string
re.match(r"Meu", texto)
```

## Padrões básicos que você vai usar toda hora

|Padrão|Significado|
|---|---|
|`\d`|dígito (0-9)|
|`\w`|letra, número ou "_"|
|`\s`|espaço em branco|
|`.`|qualquer caractere|
|`+`|1 ou mais|
|`*`|0 ou mais|
|`?`|0 ou 1 (opcional)|
|`^`|início da string|
|`$`|fim da string|

## Grupos - capturando pedacinhos específicos

```python
match = re.search(r"(\w+)@(\w+)\.com", "contato@teste.com")

print(match.group(0))  # contato@teste.com (tudo)
print(match.group(1))  # contato
print(match.group(2))  # teste
```

## Dica de ouro

Sempre use **raw strings** (aquele `r` antes das aspas, tipo `r"\d+"`). Sem ele, o Python tenta interpretar as barras invertidas como caracteres de escape (`\n`, `\t`...) e seu regex vira bagunça.

Se a expressão ficar grande e ilegível, dá uma olhada no [regex101.com](https://regex101.com/), ele te mostra visualmente o que cada parte do padrão está pegando, com explicação em tempo real. Ajuda muito a não perder a cabeça.