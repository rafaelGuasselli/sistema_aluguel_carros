from model.cliente import Cliente

class JanelaAlugaController:
	def __init__(self, gerenciador, view):
		self.view = view
		self.gerenciador = gerenciador
		self.clienteService = self.gerenciador.clienteService
		self.aluguelService = self.gerenciador.aluguelService

	def procurar(self):
		try:
			self.__procurar()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))
	
	def __procurar(self):
		cpf = self.view.getCPF()
		cliente = self.clienteService.listar(cpf=cpf)
		if cliente:
			self.view.setNome(cliente.nome)
	
	def cadastrar(self):
		try:
			self.__cadastrar()
			self.gerenciador.atualizarJanelaHome()
			self.fecharJanela()
		except Exception as erro:
			self.gerenciador.criarJanelaErro(str(erro))
	
	def __cadastrar(self):
		carro = self.view.carro
		cliente = Cliente()
		cliente.cpf = self.view.getCPF()
		cliente.nome = self.view.getNome()
		
		self.aluguelService.alugar(carro, cliente)

	def fecharJanela(self):
		self.view.destroy()	
