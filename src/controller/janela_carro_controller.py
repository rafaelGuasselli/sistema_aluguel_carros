class JanelaCarroController:
	def __init__(self, gerenciador, view):
		self.view = view
		self.gerenciador = gerenciador
		self.carroService = self.gerenciador.carroService

	def finalizar(self):
		try:
			self.__finalizar()
			self.gerenciador.atualizarJanelaHome()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))

	def __finalizar(self):
		carro = self.view.carro

		carro.modelo = self.view.getModelo()
		carro.placa = self.view.getPlaca()
		carro.cor = self.view.getCor()
		carro.taxa_hora = self.view.getTaxaHora()
		carro.taxa_dia = self.view.getTaxaDiaria()

		if carro.id != None:
			self.carroService.atualizar(carro)
		else:
			self.carroService.criar(carro)