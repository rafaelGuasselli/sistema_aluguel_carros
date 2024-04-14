import random
import string
class Funcionario:
	def __init__(self):
		self.id = None
		self.cpf = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		self.nome = ""
		self.permissoes = 0