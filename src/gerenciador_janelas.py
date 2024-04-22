import atexit

from model.funcionario import Funcionario
from model.carro import Carro

from view.janela_popup import JanelaPopup
from view.janela_login import JanelaLogin
from view.janela_home import JanelaHome
from view.janela_aluga import JanelaAluga
from view.janela_criar_carro import JanelaCriarCarro
from view.janela_editar_carro import JanelaEditarCarro

from model.carro_service import CarroService
from model.aluguel_service import AluguelService
from model.funcionario_service import FuncionarioService
from model.cliente_service import ClienteService

class GerenciadorJanelas():
	def __init__(self):
		self.carroService = CarroService()
		self.aluguelService = AluguelService()
		self.funcionarioService = FuncionarioService()
		self.clienteService = ClienteService()	
		self.criarJanelaHome()

	def criarJanelaHome(self):
		self.root = JanelaHome(self)
		self.atualizarJanelaHome()
		self.root.mainloop()

	def atualizarJanelaHome(self):
		carros = self.carroService.listar()
		funcionarioAtual = self.funcionarioService.usuarioAtual()
		self.root.inicializar(
			listaCarros=carros, 
			pagarCarros=funcionarioAtual.podeAlugar(),
			alugarCarros=funcionarioAtual.podeAlugar(), 
			editarCarros=funcionarioAtual.podeAlterarCarros(),
			removerCarros=funcionarioAtual.podeAlterarCarros(),
			adicionarCarros=funcionarioAtual.podeAlterarCarros(), 
		)

	def criarJanelaAlugarCarro(self, carro):
		JanelaAluga(self, carro)

	def criarJanelaEditarCarro(self, carro=Carro()):
		JanelaEditarCarro(self, carro)

	def criarJanelaCriarCarro(self):
		JanelaCriarCarro(self)

	def criarJanelaLogin(self):
		JanelaLogin(self)

	def criarJanelaErro(self, mensagem):
		self.criarPopup("erro", mensagem)
	
	def criarPopup(self, titulo, mensagem):
		JanelaPopup(titulo, mensagem)