import atexit

from model.funcionario import Funcionario

from view.janela_erro import JanelaErro
from view.janela_login import JanelaLogin
from view.janela_carro import JanelaCarros
from view.janela_aluga import JanelaAluga

from model.carro_service import CarroService
from model.aluguel_service import AluguelService
from model.funcionario_service import FuncionarioService
from model.cliente_service import ClienteService

class GerenciadorJanelas():
	def __init__(self):
		self.carroService = CarroService()
		self.aluguelService = AluguelService()
		self.funcionarioSerivce = FuncionarioService()	
		atexit.register(self.funcionarioSerivce.logout)

		self.criarJanelaCarros()

	def criarJanelaCarros(self):
		carros = self.carroService.listar()
		funcionarioAtual = self.funcionarioSerivce.usuarioAtual() or Funcionario()
		JanelaCarros(self, 
			listaCarros=carros, 
			alugarCarros=funcionarioAtual.podeAlterarCarros() and funcionarioAtual.podeAlterarClientes(), 
			adicionarCarros=funcionarioAtual.podeAlterarCarros(), 
			gerenciarUsuarios=funcionarioAtual.podeAlterarFuncionarios()
		)
	
	def criarJanelaAlugarCarro(self):
		pass

	def criarJanelaCriarCarro(self):
		pass


	def criarJanelaLogin(self):
		JanelaLogin(self)

	def criarJanelaErro(self, mensagem):
		JanelaErro(mensagem)
	
	def criarJanelaAluga(self, carro):
		JanelaAluga(self, carro)