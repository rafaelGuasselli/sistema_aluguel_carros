class Funcionario:
	def __init__(self):
		self.id = None
		self.cpf = ""
		self.nome = ""
		self.senha = ""
		self.permissoes = 0
	
	def podeAlterarFuncionarios(self):
		return (self.permissoes & 1<<2) > 0

	def podeAlterarCarros(self):
		return (self.permissoes & 1<<1) > 0

	def podeAlterarClientes(self):
		return (self.permissoes & 1<<0) > 0