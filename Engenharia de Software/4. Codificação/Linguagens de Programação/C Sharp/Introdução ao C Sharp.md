---
Fonte: Professor Nelio
Fonte 2: Autoria Própria Rea
---
# C Sharp

Linguagem de programação orientada a objetos, com tipagem estática, desenvolvida pela Microsoft. Define as regras sintáticas e semânticas usadas para escrever código executado sobre a plataforma .NET.

# .NET

Plataforma de desenvolvimento multiplataforma (Windows, Linux, macOS) que permite criar diversos tipos de aplicações: web, desktop, mobile, APIs, jogos, entre outros. Suporta múltiplas linguagens de programação (C#, F#, Visual Basic), todas compiladas para uma linguagem intermediária (IL, Intermediate Language) e executadas pelo CLR (Common Language Runtime).

Foi justamente para atender às necessidades dessa plataforma que a Microsoft criou o C#: uma linguagem projetada desde o início para ser a principal opção do ecossistema .NET, unindo a produtividade de linguagens de alto nível a recursos modernos de orientação a objetos.

---

# Entendendo melhor .NET

O .NET é composto por diferentes elementos que trabalham em conjunto para fornecer uma plataforma de desenvolvimento e execução de aplicações.

- `BCL` — Base Class Library
	- Conjunto de bibliotecas que fornece funcionalidades fundamentais para as aplicações .NET.

- `CLR` — Common Language Runtime
	- Ambiente de execução do .NET, funcionando de forma semelhante a uma máquina virtual.
	- Possui Garbage Collection:
		- Objetos que não são mais utilizados são automaticamente desalocados da memória.
		- Isso reduz a necessidade de o programador gerenciar manualmente a desalocação de memória durante o desenvolvimento.

## Especificação e implementação
Para entender a relação entre .NET Standard e suas diferentes tecnologias, é importante diferenciar *especificação* de *implementação*.

![[Pasted image 20260927155855.png]]

- Especificação
	- Define o que uma tecnologia deve oferecer e quais funcionalidades devem estar disponíveis.
	- Não determina necessariamente como essas funcionalidades serão construídas internamente.
	- O .NET Standard funcionava como uma especificação de APIs que uma implementação .NET deveria disponibilizar para ser compatível com aquele padrão.

- Implementação
	- É a tecnologia que efetivamente fornece aquilo que foi definido pela especificação.
	- É responsável por colocar as funcionalidades em funcionamento em uma plataforma específica.
	- Exemplos de implementações que se relacionaram com o .NET Standard:
		- `.NET Framework` (2002) -> Primeira implementação da plataforma .NET, da própria Microsoft, embora lançada anos antes da especificação .NET Standard (2016), à qual passou a dar suporte posteriormente. Muito bem avaliada, entretanto *somente funciona em sistemas Windows*.
		- `Mono` (2004) -> Abriu o .NET para a execução multiplataforma. Ainda muito usado hoje em dia! Inclusive no Xamarin e na Unity.
		- `Xamarin` (2011) -> Baseado no Mono, é utilizado para fazer aplicativos multiplataforma, inclusive em Android, iOS e macOS.
		- <span style="color: orange; font-weight: bold;">.NET Core</span> (2016) -> A mais nova (e aclamada) implementação de .NET da Microsoft. De código aberto e multiplataforma.

![[Pasted image 20260927160630.png]]

![[Pasted image 20260927161455.png]]