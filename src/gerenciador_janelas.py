import atexit

from view.janela_erro import JanelaErro
from view.janela_login import JanelaLogin
from view.janela_carro import JanelaCarros
from view.janela_aluga import JanelaAluga

from model.carro_service import CarroService
from model.aluguel_service import AluguelService
from model.funcionario_service import FuncionarioService
from model.cliente_service import ClienteService

class GerenciadorJanelas:
	def __init__(self):
		self.carroService = CarroService()
		self.aluguelService = AluguelService()
		self.funcionarioService = FuncionarioService()
		self.clienteService = ClienteService()
		atexit.register(self.funcionarioService.logout)
	
	def criarJanelaLogin(self):
		JanelaLogin(self)
	
	def criarJanelaCarros(self):
		JanelaCarros(self, listaCarros=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], alugarCarros=True, adicionarCarros=True, gerenciarUsuarios=True)

	def criarJanelaErro(self, mensagem):
		JanelaErro(mensagem)
	
	def criarJanelaAluga(self, carro):
		JanelaAluga(self, carro)