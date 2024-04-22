class Funcionario:
	def __init__(self):
		self.id = None
		self.nome = ""
		self.senha = ""
		self.permissoes = 0
	
	def podeAlterarFuncionarios(self):
		return (self.permissoes & 1<<2) > 0

	def podeAlterarCarros(self):
		return (self.permissoes & 1<<1) > 0

	def podeAlugar(self):
		return (self.permissoes & 1<<0) > 0

	def __str__(self):
		return "Nome: {}, Permissões: {}".format(self.nome, self.permissoes)