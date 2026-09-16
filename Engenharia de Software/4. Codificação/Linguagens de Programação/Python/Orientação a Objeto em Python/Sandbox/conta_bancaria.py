from rich import print
from rich.table import Table
from rich.traceback import install
import re
install()

class ContaBancaria():
	def __init__(self, nome, numero, valor_inicial):
		self.nome_titular = nome
		self.numero = numero
		self.saldo = valor_inicial

	def informar_saldo(self):
		tabela = Table(title="Conta", style="blue")
		tabela.add_column("Info")
		tabela.add_column("Valor")
		tabela.add_row("Nome", f"{self.nome_titular}")
		tabela.add_row("Número", f"{self.numero}")
		tabela.add_row("Saldo", f"[blue]{self.saldo}[/]")
		
		print(tabela)

	def depositar_valor(self, valor):
		if valor <= 0:
			print(f"[red]VALOR NÃO PERMITIDO[/]")
			return
		self.saldo += valor
		self.informar_saldo()

	def sacar_valor(self, valor):
		if valor <= 0:
			print(f"[red]VALOR NÃO PERMITIDO[/]")
			return
		if self.saldo <= 0 or self.saldo < valor:
			print(f"[red]SALDO INSUFICIENTE[/]: {self.saldo}")
			return
		self.saldo -= valor
		self.informar_saldo()

conta01 = ContaBancaria("Rea", 508, 1000)
continuar = True

while continuar == True:
	opcao = input("\nSelecione uma opcao (Consultar, Depositar, Sacar, Sair): ")
	match opcao:
		case cmd if re.fullmatch(r"consultar\s*", cmd, re.IGNORECASE):
			conta01.informar_saldo()
		case cmd if re.fullmatch(r"depositar\s*", cmd, re.IGNORECASE):
			valor = int(input("Insira o valor: "))
			conta01.depositar_valor(valor)
		case cmd if re.fullmatch(r"sacar\s*", cmd, re.IGNORECASE):
			valor = int(input("Insira o valor: "))
			conta01.sacar_valor(valor)
		case cmd if re.fullmatch(r"sair\s*", cmd, re.IGNORECASE):
			continuar = False
			break
		case _ :
			print("[red]Opção inválida[/].")