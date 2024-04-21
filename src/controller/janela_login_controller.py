class JanelaLoginController:
	def __init__(self, gerenciador, view):
		self.view = view
		self.gerenciador = gerenciador
		self.funcionarioService = self.gerenciador.funcionarioSerivce
		
	def login(self):
		try:
			self.__login()
			self.gerenciador.criarJanelaCarros()
			self.fecharJanela()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))

	def __login(self):
		cpf = self.view.getCPF()
		senha = self.view.getSenha()
		self.funcionarioSerivce.login(cpf, senha)

	def fecharJanela():
		self.destroy()		
