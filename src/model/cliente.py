class Cliente:
	def __init__(self):
		self.id = None
		self.cpf = ""
		self.nome = ""

	def __str__(self):
		return "CPF: {}, Nome: {}".format(self.cpf, self.nome)