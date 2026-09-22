from rich import print
from rich.panel import Panel
from rich.traceback import install
from rich.align import Align
install()

class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def mostrar_etiqueta(self) -> str:
        etiqueta = Panel(Align.center(f"[white]{self.preco}[/]"), title="Etiqueta", style="blue", width=10, title_align="center")
        return etiqueta

celular = Produto("Iphone", 5284)

print(celular.mostrar_etiqueta())

# se quiser fazer melhor que essa porcaria q eu fiz: https://youtu.be/c9W6E4Bxv5E?list=PLHz_AreHm4dn_RXXoa3Ameh77f95Hgwv3