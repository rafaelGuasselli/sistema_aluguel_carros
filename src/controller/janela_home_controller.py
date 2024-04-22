class JanelaHomeController:
	def __init__(self, gerenciador, view):
		self.view = view
		self.gerenciador = gerenciador
		self.funcionarioService = self.gerenciador.funcionarioService
		self.aluguelService = self.gerenciador.aluguelService
		self.carroService = self.gerenciador.carroService


	def pagar(self,carro):
		try:
			self.__pagar(carro)
			self.gerenciador.atualizarJanelaHome()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))

	def __pagar(self, carro):
		preco = self.aluguelService.pagar(carro)
		self.gerenciador.criarPopup("Pagar", "R${:.2f}".format(preco))

	def logout(self):
		try:
			self.gerenciador.funcionarioService.logout()
			self.gerenciador.atualizarJanelaHome()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))

	def telaLogin(self):
		try:
			self.gerenciador.criarJanelaLogin()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))
	
	def telaUsuarios(self):
		return
	
	def telaCriarCarros(self):
		try:
			self.gerenciador.criarJanelaCriarCarro()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))
	
	def alugar(self,carro):
		try:
			self.__alugar(carro)
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))

	def __alugar(self, carro):
		carro = self.carroService.listar(carro=carro)
		if carro and carro.estaAlugado():
			raise Exception("Carro já está alugado!")

		self.gerenciador.criarJanelaAlugarCarro(carro)

	def editar(self, carro):
		try:
			self.gerenciador.criarJanelaEditarCarro(carro)
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))

	def remover(self,carro):
		try:
			self.__remover(carro)
			self.gerenciador.atualizarJanelaHome()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))
	
	def __remover(self, carro):
		self.carroService.deletar(carro)