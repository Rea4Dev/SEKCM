from rich import print

class Funcionario:
    def __init__(self, nome: str, setor: str, cargo: str) -> None:
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> str:
        return (f"Olá! Eu sou o [blue]{self.nome}[/blue], {self.cargo} na {self.setor}")

pessoa1 = Funcionario("João", "DEM", "Estagiário")

print(pessoa1.apresentar())

# se qse fazer melhor: https://www.youtube.com/watch?v=B0DccRlwmS8&list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3&index=10&pp=iAQB