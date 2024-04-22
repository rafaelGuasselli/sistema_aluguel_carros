class JanelaEditarController:
	def __init__(self, gerenciador, view):
		self.view = view
		self.gerenciador = gerenciador
		self.funcionarioService = self.gerenciador.funcionarioService

	def alugar(self,carro):
		print(carro)
		try:
			self.gerenciador.criarJanelaAlugarCarro(carro)
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))

	def editar(self, carro):
		print("HAHAHAHHAHAHAHA")
		try:
			self.gerenciador.criarJanelaEditarCarro(carro)
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))

	def remover(carro):
		pass

	def pagar(self,carro):
		try:
			self.__pagar(carro)
			self.gerenciador.atualizarJanelaCarros()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))

	def __pagar(self, carro):
		carro.cliente_id = None
		self.gerenciador.carroService.atualizar(carro)

	
	def logout(self):
		try:
			self.gerenciador.funcionarioService.logout()
			self.gerenciador.atualizarJanelaCarros()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))

	def telaLogin(self):
		try:
			self.gerenciador.criarJanelaLogin()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))
	