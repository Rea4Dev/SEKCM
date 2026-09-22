---
Fonte: Gustavo Guanabara
Fonte 2: Autoria Própria Rea
---
# Acesso a dados encapsulados
Existem duas maneiras de permitir o acesso aos dados encapsulados:

## 1. Uso de Getters e Setters
![[Pasted image 20260921185153.png]]

```python
class Avaliacao:

    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo protected (#)

    # Métodos Acessores
    def get_nota(self): # Método Getter
        return self._nota

    def set_nota(self, valor): # Método Setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida!")
```


## 2. Uso do decorador *@property*
