from datetime import date, datetime

class Carro:
	def __init__(self):
		self.id = 0
		self.cor = ""
		self.taxa_hora = 0
		self.placa = ""
		self.modelo = ""
		self.taxa_dia = 0
		self.cliente_id = None
		self.data_aluguel = None

	def calcularPreco(self):
		hoje = datetime.combine(date.today(), datetime.min.time())
		diferenca = hoje - self.data_aluguel
		preco = 0
		preco += diferenca.days * self.taxa_dia
		preco += diferenca.seconds//3600 * self.taxa_hora
		return preco

	def estaAlugado(self):
		return self.cliente_id != None

	def __str__(self):
		return "Modelo: {}, Cor: {}, Alugado: {}, Estimativa: {}, Taxa por dia: {}, Taxa por hora: {} cliente id: {}".format(self.modelo, self.cor, self.cliente_id != None, self.data_aluguel, self.taxa_dia, self.taxa_hora, self.cliente_id)