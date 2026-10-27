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
O uso do decorador @property permite criar um ==atributo validável==.
Com essa técnica, é possível manipular o dado encapsulado como se fosse um atributo comum, mantendo a proteção e a lógica de validação por trás.

```python
class Avaliacao:

    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    @property
    def nota(self): # Getter
        return self._nota

    @nota.setter
    def nota(self, valor): # Setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida!")
```

## Principais diferenças:

* **Getters e Setters:** É a abordagem tradicional POO, exigindo a chamada explícita de métodos como `objeto.get_nota()` e `objeto.set_nota(valor)`.
* **@property:** Oferece uma sintaxe mais elegante e pythônica, onde o acesso é feito via `objeto.nota` diretamente, disparando os métodos de controle automaticamente.
