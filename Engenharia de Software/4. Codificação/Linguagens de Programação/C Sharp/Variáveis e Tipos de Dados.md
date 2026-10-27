# Variáveis e Tipos de Dados C Sharp

errata: SByte e não Sbyte. A propósito, para usar o do .Net você precisa importar `System`.
![[Pasted image 20260929212833.png]]
 
- Ao trabalhar com long, deixe L no final do número `159314L` (boa prática).

- Ao trabalhar com char, caractere único, você precisa delimitar com aspas simples `'C'`. Funciona também se você colocar o unicode `'\u0041'`.

- Ao trabalhar com floar, você precisa colocar f no final do número `3.14f`. Caso contrário, ele vai considerar como double.
## var
`var` é a declaração de variável com ==tipo inferido==: o compilador descobre o tipo a partir do valor atribuído e o fixa ==em tempo de compilação==.

```Cs
var numero = 10;          // int
var texto  = "olá";       // string
var preco  = 19.90m;      // decimal
```

Não é ausência de tipo. A variável ==tem tipo==, só não precisa ser escrito por você. O código compilado é ==idêntico== ao de `int numero = 10;`.

### Tipagem estática, não dinâmica
Depois de inferido, o tipo ==não muda==:

```csharp
var numero = 10;
numero = 20;          // ok
numero = "texto";     // erro CS0029: string não converte para int
```

Isso é diferente de linguagens como JavaScript ou Python, onde a variável pode trocar de tipo. Em C# o tipo é definido na declaração, seja escrito (`int`) ou inferido (`var`).
