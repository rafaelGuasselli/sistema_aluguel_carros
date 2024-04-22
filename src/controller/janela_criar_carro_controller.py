from model.carro import Carro

class JanelaCriarCarroController:
	def __init__(self, gerenciador, view):
		self.view = view
		self.gerenciador = gerenciador
		self.carroService = self.gerenciador.carroService
	
	def finalizar(self):
		carro = self.view.carro or Carro()
		try:
			carro.cor = self.view.getCor()
			carro.placa = self.view.getPlaca()
			carro.modelo = self.view.getModelo()
			carro.taxa_hora = int(self.view.getTaxaHora())
			carro.taxa_dia = int(self.view.getTaxaDiaria())
			self.carroService.criar(carro=carro)
			self.gerenciador.atualizarLista()
			self.fecharJanela()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))
	
	
	def fecharJanela(self):
		self.view.destroy()