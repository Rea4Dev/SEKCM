---
Fonte: Professor Nelio
Fonte 2: Autoria Própria Rea
---
# Split()
Divide uma `string` em partes menores a partir de um caractere ou sequência de caracteres delimitadora.

O resultado é um array (`string[]`) contendo cada parte:
```csharp
string s = "batata tomate abacaxi";

string[] cortado = s.Split(' ');
```

Nesse caso, o espaço `' '` é utilizado como delimitador:
```text
"batata"   "tomate"   "abacaxi"
```

Cada palavra ocupa uma posição no array, que pode ser acessada pelo índice:
```csharp
cortado[0] // "batata"
cortado[1] // "tomate"
cortado[2] // "abacaxi"
```

# Parse
Converte uma string para um tipo numérico, desde que o conteúdo esteja em um formato válido para esse tipo.

```csharp
int n1 = int.Parse(Console.ReadLine());
```
