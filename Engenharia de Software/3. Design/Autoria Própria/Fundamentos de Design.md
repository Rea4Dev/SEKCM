---
Fonte: SWEBOK
Fonte 2: Roger S. Pressman
Fonte 3: Sommerville
---

# 1. SWEBOK

O SWEBOK é provavelmente a referência que oferece ==a definição mais precisa== e que a mais consideraremos para estudar e referenciar o tema.

Ele define Design ==simultaneamente como processo e como resultado==.

`Como processo`:
> "the process of defining the architecture, components, interfaces, and other characteristics of a system or component"

`Como resultado`, o Design é aquilo que foi produzido por esse processo.

Dentro do ciclo de vida, o SWEBOK caracteriza o Design como ==a atividade em que os requisitos de software são analisados para produzir uma descrição da estrutura interna do software que servirá de base para sua construção==.

Essa definição estabelece uma fronteira conceitual importante:
```text
Requisitos → Design → Construção
```

O SWEBOK divide o Design em duas grandes atividades:

1. `Design arquitetural`
    - define a estrutura e organização de alto nível;
    - identifica os componentes.

2. `Design detalhado`
    - especifica cada componente em nível suficiente para permitir sua construção.

Além disso, o SWEBOK apresenta Design, em sentido geral, como uma forma de resolução de problemas, envolvendo conceitos como *objetivos, restrições, alternativas, representações e soluções*.

---

# 2. Pressman

Para Pressman, Design é a atividade na qual o modelo de requisitos é transformado em um modelo técnico que representa a solução a ser construída.

Em termos mais orgânicos:
Design é o processo de transformar aquilo que o software precisa fazer em uma representação de como o software será estruturado e construído.

Essa transformação envolve, entre outras coisas:
- estruturas de dados;
- arquitetura;
- interfaces;
- componentes;
- detalhes necessários para implementação;
- decisões de projeto que precisam ser avaliadas quanto à qualidade.

Pressman coloca uma distinção importante: o Design não é simplesmente "desenhar uma solução". Ele produz uma representação de engenharia que pode ser analisada, revisada e posteriormente implementada.

Um trecho particularmente útil é:
> "A software design creates meaningful engineering representation [...] of some software product that is to be built." (Pressman, Software Engineering, 7ª ed., cap. 8, "Design Concepts").

E ele explicita a transformação:
> "the software requirements model [...] is transformed into design models"

Ou seja, para Pressman, existe uma relação direta entre o modelo de requisitos e o modelo de Design.

---

# 3. Sommerville

Sommerville segue uma linha bastante compatível com as duas anteriores.

Para ele, um software design é uma descrição de:

- estrutura do software;
- modelos e estruturas de dados;
- interfaces entre componentes;
- e, em alguns casos, algoritmos.

Um trecho bastante direto é:
> "A software design is a description of the structure of the software to be implemented" (Sommerville, Software Engineering, 10ª ed., cap. 2).

Mas há uma característica de Sommerville muito importante: ==ele não apresenta Design como algo necessariamente linear==.

Os designers desenvolvem o Design em ==estágios==, adicionando detalhes ==progressivamente e retornando constantemente a decisões anteriores para modificá-las==.

Isso combina muito bem com a ideia estabelecida no Planejamento de que atividades da Engenharia de Software podem ser iterativas e adaptativas.

Sommerville também faz uma observação importante sobre processos ágeis: *Design e implementação podem ser intercalados*, sem que isso signifique que o Design desapareceu. O Design continua existindo; o que muda é sua forma de realização e documentação.