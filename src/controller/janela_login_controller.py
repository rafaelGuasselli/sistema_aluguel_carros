class JanelaLoginController:
	def __init__(self, gerenciador, view):
		self.view = view
		self.gerenciador = gerenciador
		self.funcionarioService = self.gerenciador.funcionarioService
		
	def login(self):
		try:
			self.__login()
			self.gerenciador.atualizarJanelaCarros()
			self.fecharJanela()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))

	def __login(self):
		nome = self.view.getNome()
		senha = self.view.getSenha()
		self.funcionarioService.login(nome, senha)

	def fecharJanela(self):
		self.view.destroy()