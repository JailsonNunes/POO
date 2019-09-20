class Pessoa:
	def __init__(self,nome, endereco,telefone):
		self.nome = nome;
		self.endereco = endereco;
		self.telefone = telefone;

	def imprimir(self):
		print("Nome:",self.nome)
		print("Endereco:",self.endereco)
		print("Telefone:",self.telefone)