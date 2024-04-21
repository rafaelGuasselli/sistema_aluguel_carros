class Carro:
	def __init__(self):
		self.id = 0
		self.cor = ""
		self.multa = 0
		self.placa = ""
		self.modelo = ""
		self.taxa_dia = 0
		self.cliente_id = None
		self.estimativa_devolucao = None

	def __str__(self):
		return "Modelo: {}, Cor: {}, Alugado: {}, Estimativa: {}, Taxa por dia: {}, Multa: {}".format(self.modelo, self.cor, self.cliente_id != None, self.estimativa_devolucao, self.taxa_dia, self.multa)