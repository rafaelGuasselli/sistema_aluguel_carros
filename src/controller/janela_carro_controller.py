class JanelaCarroController:
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

	def editar(carro):
		pass

	def remover(carro):
		pass
	
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
	