import atexit

from view.janela_erro import JanelaErro
from view.janela_login import JanelaLogin
from view.janela_carro import JanelaCarros

from model.carro_service import CarroService
from model.aluguel_service import AluguelService
from model.funcionario_service import FuncionarioService

class GerenciadorJanelas:
	def __init__(self):
		self.carroService = CarroService()
		self.aluguelService = AluguelService()
		self.funcionarioSerivce = FuncionarioService()
		atexit.register(self.funcionarioSerivce.logout)
	
	def criarJanelaLogin(self):
		JanelaLogin(self)
	
	def criarJanelaCarros(self):
		JanelaCarros(self, listaCarros=["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], alugarCarros=True, adicionarCarros=True, gerenciarUsuarios=True)

	def criarJanelaErro(self, mensagem):
		JanelaErro(mensagem)