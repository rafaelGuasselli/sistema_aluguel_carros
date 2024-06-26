from datetime import date, datetime

class Carro:
	def __init__(self):
		self.id = None
		self.cor = ""
		self.taxa_hora = None
		self.placa = ""
		self.modelo = ""
		self.taxa_dia = None
		self.cliente_id = None
		self.data_aluguel = None

	def calcularPreco(self):
		if (not isinstance(self.data_aluguel, datetime)):
			return 0

		if self.taxa_dia == None or self.taxa_hora == None:
			return 0

		hoje = datetime.now()
		diferenca = hoje - self.data_aluguel
		preco = 0
		preco += diferenca.days * self.taxa_dia
		preco += diferenca.seconds/3600 * self.taxa_hora
		return preco

	def estaAlugado(self):
		return self.cliente_id != None

	def __str__(self):
		return "Modelo: {}, Cor: {}, Alugado: {}, Data aluguel: {}, Taxa por dia: {}, Taxa por hora: {}, Cliente id: {}".format(self.modelo, self.cor, self.cliente_id != None, self.data_aluguel, self.taxa_dia, self.taxa_hora, self.cliente_id)