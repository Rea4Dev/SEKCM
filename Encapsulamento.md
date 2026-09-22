---
Fonte: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# Encapsulamento

Visa manter a *integridade* do sistema, protegendo o *estado interno do objeto* contra *interferência externa não regulamentada*. 


Minha definição favorita é a do professor:
> Encapsular é proteger o sistema para que ==mesmo a pessoa autorizada== não cause problemas mexendo em coisas que não deve; deixando disponível para ela apenas o que deve.


Ou seja, deixar exposto ao usuário apenas a `interface pública`; somente o essencial. 

Mantemos os detalhes complexos de implementação protegidos internamente, ==oferecendo apenas os meios necessários para que o usuário interaja com o objeto de maneira segura e eficiente==, garantindo que a integridade do sistema não seja comprometida por interferências externas.

![[Pasted image 20260920162550.png | 250 ]] ![[Pasted image 20260920162605.png | 250]]



## Encapsular

- *Segurança e Controle*: Protege o estado interno do objeto, evitando interferências externas indevidas e garantindo que apenas acessos autorizados possam modificar os dados.

- *Facilidade de Manutenção*: Permite modificar o funcionamento interno de uma classe sem afetar o restante do sistema, desde que a interface pública permaneça inalterada.

- *Flexibilidade de reutilização*: Facilita o reaproveitamento de classes encapsuladas em outros projetos ou contextos com pouca ou nenhuma necessidade de adaptação.

- *Redução de Efeitos Colaterais*: Impede que o acesso direto a componentes internos cause danos ou comportamentos inesperados, garantindo que o objeto se comporte de maneira previsível.

## Não encapsular

![[Pasted image 20260921181648.png]]

Não encapsular uma classe é conceitualmente equivalente ao bando dizer:
> sacar? Vai ali **sozinho** naquele cofre **sem câmeras** e pega o que precisa. 🤡


```python
conta1 = ContaBancaria(id=111, nome="Rea", saldo=5000)

conta1.saldo = 9999999999 #👹
```
Como não há encapsulamento, foi possível a instância modificar o atributo saldo (que não deveria poder).

# Visibilidade dos atributos
Existem três tipos de visibilidade para atributos em linguagens POO:
- público <span style="color: yellow; font-size:120%;">+</span> 
![[Pasted image 20260921182727.png | 200]]
- protegido <span style="color: yellow; font-size:120%;">#</span>
![[Pasted image 20260921182823.png | 200]]
- privado <span style="color: yellow; font-size:120%;">-</span>
![[Pasted image 20260921182856.png | 200]]




Em Python:
![[Pasted image 20260921183443.png]]
- público (normal)
- protegido ( _ )
- privado ( _ _ )



# Encapsulamento e Visibilidade em Python
Basicamente, apesar do conceito existir em Python, ele não restringe como outras linguagens fazem. 
Ou seja, na prática, tudo é público.
Apesar de que na semântica, você tem um comportamento declarado a seguir.


Isso pois python segue o *Consenting Adults*, que preza "Liberdade com Responsabilidade". Então você é avisado para não modificar um privado na main, por exemplo, mas confiamos em você que ser avisado é o suficiente para não fazer (🤡).