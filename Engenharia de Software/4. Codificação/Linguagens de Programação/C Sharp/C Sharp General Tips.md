---
Fonte: Autoria Própria Rea
---
# C Sharp General Tips
![[Pasted image 20261002174123.png]]

## Write() e WriteLine()
Ambos exibem informações no console.
- `Console.Write()` → escreve o conteúdo e mantém o cursor na ==mesma linha==.
- `Console.WriteLine()` → escreve o conteúdo e move o cursor para a próxima linha.
```csharp
Console.Write("Olá ");
Console.Write("mundo!");
// Olá mundo!

Console.WriteLine("Olá");
Console.WriteLine("mundo!");
// Olá
// mundo!
```

## CultureInfo.InvariantCulture
Faz com que operações de formatação e conversão usem uma ==cultura neutra== e consistente, independentemente das configurações regionais do computador.

É útil principalmente para lidar com números, datas e textos que precisam manter o mesmo formato em diferentes ambientes.

Requer o import:
```csharp
using System.Globalization;
```

Exemplo:
```csharp
double preco = 19.90;

Console.WriteLine(preco.ToString(CultureInfo.InvariantCulture));
// 19.9
```

## Placeholder :F2
É um especificador de formato usado para exibir um número com exatamente 2 casas decimais.

Em uma string interpolada, aparece como `:F2`:
```csharp
double preco = 19.9;

Console.WriteLine($"R$ {preco:F2}");
// R$ 19,90
```

O `F` significa `Fixed-point` (ponto fixo) e o `2` indica a quantidade de casas decimais.

## Casting
Conversão explícita de um valor de um tipo para outro tipo compatível.
É necessário informar o tipo desejado entre parênteses antes do valor:

```csharp
double a = 5.1;
float b = (float)a;
```

Nesse caso, `(float)` realiza o casting de `double` para `float`. Como `float` possui menor precisão, pode ocorrer perda de informação.

## ReadLine()
Lê a entrada padrão até a quebra de linha e retorna o conteúdo lido na forma de `string`.

```csharp
string texto = Console.ReadLine();
```

É utilizado principalmente para receber dados digitados pelo usuário no console.

## Debugging
![[Pasted image 20261006191048.png]]

## Auto-Identação
É possível ordenar a identação através de um comando: `CTRL + K + D`.

## Convenção para nomes
C# possui convenções de nomenclatura para manter o código consistente e legível.

- `PascalCase` → primeira letra de cada palavra em maiúscula. Usado em ==classes, métodos, propriedades e namespaces==.
- `camelCase` → primeira palavra começa em minúscula e as seguintes em maiúscula. Usado em ==variáveis e parâmetros==.
- `UPPER_CASE` → geralmente reservado para constantes em algumas convenções, embora `PascalCase` seja a convenção recomendada pelo C#.

Não categorizamos especificamente atributos, e sim se é publico, privado etc:
- Campos privados e protegidos → `camelCase`  
- Propriedades e campos públicos → `PascalCase`

```csharp
class ContaBancaria
{
    const double TaxaJuros = 0.05;

    public void CalcularSaldo(double valorInicial)
    {
        double saldoAtual = valorInicial;
    }
}
```

Essas convenções não são obrigatórias para o compilador, mas seguem o padrão adotado pelo ecossistema .NET e facilitam a leitura e manutenção do código.