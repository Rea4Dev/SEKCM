---
Fonte: Gustavo Guanabara
---
# Por que a Programação Orientada a Objetos (POO) existe?
A POO surge como uma resposta evolutiva às limitações das formas tradicionais de armazenamento e manipulação de dados na programação. O raciocínio central é que objetos são "variáveis evoluídas".

## A Evolução das Variáveis

Para entender a necessidade da POO, acompanhamos a trajetória da estrutura de dados:

1. **Variáveis Simples:** Espaços na memória que guardam apenas um valor por vez. Se um novo valor é atribuído, o anterior é descartado.
2. **Variáveis Compostas (Listas):** Evolução necessária para armazenar múltiplos valores, utilizando índices numéricos. O problema aqui é a complexidade de gerenciar esses índices.
3. **Variáveis Compostas Nomeadas (Dicionários):** Evolução das listas onde os índices são literais (nomes), facilitando a identificação dos dados.

## O Grande Desafio: Dados vs. Funções

Mesmo com estruturas avançadas como dicionários, um problema persiste na programação estruturada: ==a separação entre dados e funções.==
![[Pasted image 20260825200828.png | center | 400]]

*   Os dados (atributos) vivem em um lugar.
*   As funcionalidades (métodos) que manipulam esses dados vivem em outro lugar, separadas do dado em si.

## A Solução: O Conceito de Objeto

A POO resolve esse hiato ao unificar ==dados + funcionalidades== em uma única estrutura. 

*   **Definição:** Um [[objeto ]]é uma variável que, além de guardar dados, possui a capacidade de executar funcionalidades (tarefas) sobre esses mesmos dados.
*   **Classes como Molde:** A [[classe]] atua como o molde (a forma do biscoito), permitindo a criação (instanciação) de diversos objetos a partir de uma única definição de estrutura e comportamento.
*   **O papel do Self:** O uso do *self* é a forma como a linguagem garante que a funcionalidade saiba exatamente qual objeto (instância) está chamando aquele método, evitando confusão entre diferentes instâncias da mesma classe.

**Conclusão:** A POO existe para organizar o código de forma mais intuitiva, agrupando o estado (dados) e o comportamento (funcionalidades) em uma entidade coesa, tornando o desenvolvimento de sistemas complexos mais gerenciável e eficiente.