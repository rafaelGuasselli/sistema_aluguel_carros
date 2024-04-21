class JanelaCarroController:
	def __init__(self, gerenciador, view):
		self.view = view
		self.gerenciador = gerenciador
		self.funcionarioService = self.gerenciador.funcionarioService
		
	def login(self):
		self.funcionarioService = self.gerenciador.funcionarioSerivce
	
	def alugar(carro):
		try:
			self.gerenciador.criarJanelaAlugarCarro()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))
	
	def editar(carro):
		pass

	def __login(self):
		cpf = self.view.getCPF()
		senha = self.view.getSenha()
		self.funcionarioService.login(cpf, senha)
	

	def telaLogin(self):
		try:
			self.gerenciador.criarJanelaLogin()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))

	def fecharJanela(self):
		self.view.destroy()		
	def remover(carro):
		pass
