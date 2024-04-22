import atexit

from model.funcionario import Funcionario

from view.janela_popup import JanelaPopup
from view.janela_login import JanelaLogin
from view.janela_carro import JanelaCarros
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
		# atexit.register(self.funcionarioService.logout)
		self.criarJanelaCarros()

	def criarJanelaCarros(self):
		carros = self.carroService.listar()
		funcionarioAtual = self.funcionarioService.usuarioAtual() or Funcionario()
		self.root = JanelaCarros(self, 
			listaCarros=carros, 
			alugarCarros=funcionarioAtual.podeAlterarCarros() and funcionarioAtual.podeAlterarClientes(), 
			adicionarCarros=funcionarioAtual.podeAlterarCarros(), 
			editarCarros=funcionarioAtual.podeAlterarCarros(),
			gerenciarUsuarios=funcionarioAtual.podeAlterarFuncionarios(),
			pagarCarros=funcionarioAtual.podeAlterarCarros()
		)

		self.root.mainloop()

	def atualizarJanelaCarros(self):
		carros = self.carroService.listar()
		funcionarioAtual = self.funcionarioService.usuarioAtual() or Funcionario()
		self.root.inicializar(
			listaCarros=carros, 
			alugarCarros=funcionarioAtual.podeAlterarCarros() and funcionarioAtual.podeAlterarClientes(), 
			adicionarCarros=funcionarioAtual.podeAlterarCarros(), 
			editarCarros=funcionarioAtual.podeAlterarCarros(),
			gerenciarUsuarios=funcionarioAtual.podeAlterarFuncionarios(),
			pagarCarros=funcionarioAtual.podeAlterarCarros()
		)
	
	def criarJanelaAlugarCarro(self, carro):
		JanelaAluga(self, carro)

	def criarJanelaCriarCarro(self):
		pass
	
	def criarJanelaEditarCarro(self, carro):
		print("KAKAKKAKAKA")
		JanelaEditarCarro(self, carro)

	def criarJanelaLogin(self):
		JanelaLogin(self)

	def criarJanelaErro(self, mensagem):
		self.criarPopup("erro", mensagem)
	
	def criarPopup(self, titulo, mensagem):
		JanelaPopup(titulo, mensagem)