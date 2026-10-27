# Cruzamento de tipos

Em operações aritméticas (`+ - * / %`), C# *não opera tipos menores que `int`*. 

Antes de calcular, `sbyte`, `byte`, `short`, `ushort` e `char` são convertidos para `int` (_promoção numérica_). Por isso `sbyte + sbyte` resulta em `int`.

```csharp
sbyte var1 = 10;
sbyte var2 = 20;

var r = var1 + var2;                           // r é int
Console.WriteLine((var1 + var2).GetType());   // System.Int32
```

Por que existe:
- A CPU trabalha nativamente com 32 bits, então `int` é o menor tipo com operadores aritméticos definidos.
- Evita estouro silencioso: ==100 + 100== em `sbyte` passaria de 127, mas em `int` dá 200 sem problema.

## Como deduzir o tipo do resultado
**Passo 1:** tipos menores que `int` (`sbyte`, `byte`, `short`, `ushort`, `char`) viram `int`.
**Passo 2:** o resultado é o ==maior tipo== da escada abaixo, entre os dois operandos:
```
int < uint < long < ulong < float < double < decimal
```
