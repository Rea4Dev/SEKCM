---
Fonte: SWEBOK
Fonte 2: Roger S. Pressman
Fonte 3: Sommerville
---
# 1. SWEBOK

O SWEBOK é mais formal e explícito. Ele apresenta três sentidos complementares para software requirement:

- uma ==condição ou capacidade necessária ao usuário para resolver um problema ou alcançar um objetivo==;

- uma ==condição ou capacidade que o sistema ou componente deve possuir para satisfazer contrato, padrão, especificação ou outro documento formal==;

- a ==representação documentada de uma dessas condições ou capacidades==.

O SWEBOK ainda generaliza isso dizendo:

> “At its most basic, a software requirement is a property that must be exhibited to solve a real-world problem.”

Em essência: requisito é uma *necessidade, condição ou capacidade que o software precisa satisfazer para resolver um problema ou atingir um objetivo*, podendo também ser a sua representação documentada.

---

# 2. Pressman

Para Pressman, requisito é ==aquilo que descreve o que o sistema deve fazer ou quais restrições deve satisfazer==. Ele trabalha com a ideia de que os requisitos *podem variar* de uma *descrição abstrata* de um serviço/restrição *até uma especificação funcional* bastante detalhada.

Um ponto importante em Pressman é a **distinção** entre `o que` o sistema deve fazer e `como` ele será construído: durante a análise de requisitos, ==o foco deve permanecer no what, não no how==.

> “Requirements are used to describe all aspects of a system.”

E também:

> “They may range from a high-level abstract statement of a service or of a system constraint to a detailed mathematical functional specification.”

Em essência: ==requisito é uma descrição do que é necessário que o sistema ofereça, faça ou respeite==.

---

# 3. Sommerville

Sommerville coloca a definição de maneira muito direta:

> “The requirements for a system are the descriptions of what the system should do—the services that it provides and the constraints on its operation.”

Ou seja, para ele, requisitos são ==descrições dos serviços que o sistema deve fornecer e das restrições sob as quais ele deve operar==.

Ele também diferencia níveis:
- `User requirements`: descrição mais abstrata, voltada aos usuários;
- `System requirements`: descrição mais detalhada das funções, serviços e restrições que deverão ser implementados.

Em essência: requisito é uma descrição de um serviço que o sistema deve fornecer ou de uma restrição que deve respeitar.

---

# A síntese das três

Dá para abstrair muito bem assim:

> Requisito de software é uma descrição de uma necessidade, capacidade, serviço ou restrição que o software deve satisfazer para atender às necessidades dos stakeholders, resolver um problema ou alcançar um objetivo.

E existe uma ideia comum muito importante nas três fontes:

==Requisito descreve o que é necessário, não a solução de como implementá-lo==.

| Fonte       | Ênfase principal                                                                            |
| ----------- | ------------------------------------------------------------------------------------------- |
| Pressman    | O que o sistema deve fazer e quais restrições deve satisfazer                               |
| SWEBOK      | Necessidade/capacidade/condição necessária para resolver um problema ou atingir um objetivo |
| Sommerville | Serviços que o sistema fornece + restrições sob as quais opera                              |

- SWEBOK como definição mais ==rigorosa==
- Pressman para reforçar a ideia de “==o quê, não como==”
- Sommerville para tornar a definição ==operacional por meio de “serviços + restrições==”.
