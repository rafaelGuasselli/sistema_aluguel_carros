import random
import string

class Carro:
	def __init__(self):
		self.id = 0
		self.cor = ""
		self.multa = 0
		self.placa = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		self.modelo = ""
		self.taxa_dia = 0
		self.cliente_id = None
		self.estimativa_devolucao = None