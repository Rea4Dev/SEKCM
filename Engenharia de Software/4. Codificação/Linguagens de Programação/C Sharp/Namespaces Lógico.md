# Namespaces
Agrupamento *lógico* de classes relacionadas.

Em uma aplicação, posso ter classes que representam diferentes conceitos e responsabilidades do sistema. Os namespaces permitem organizar essas classes logicamente, facilitando sua localização e evitando conflitos de nomes.

> Namespace é uma ==forma de organizar classes logicamente dentro do código==. Ele não é, por si só, uma camada ou uma pasta física do projeto, embora seja comum que a organização dos namespaces acompanhe a organização das pastas.

![[Pasted image 20260927204100.png]]
## Entities
Posso ter classes que representam minhas ==entidades de negócio== (Entities), ou seja, ==conceitos do domínio que o sistema precisa representar e, em muitos casos, armazenar==.

Exemplos de entidades de negócio:
- Clientes
- Produtos
- Pedidos
- Funcionários
- Categorias

Essas classes podem ser organizadas em um namespace chamado `Entities`.

## Services
Também posso ter classes responsáveis por ==implementar serviços e regras de negócio da aplicação==.

Por exemplo:
- `CustomerService`
- `OrderService`
- `ProductService`

Essas classes podem ser organizadas em um namespace chamado `Services`.

## Repositories
Também posso ter classes responsáveis pelo ==acesso e persistência dos dados==, como ==operações de consulta, inclusão, alteração e exclusão==.

Por exemplo:
- `CustomerRepository`
- `OrderRepository`
- `ProductRepository`

Essas classes podem ser organizadas em um namespace chamado `Repositories`.