import random
import string
import unittest
from src.model.cliente import Cliente
from src.model.cliente_service import ClienteService
from src.model.funcionario_service import FuncionarioService

class TestClienteService(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestClienteService, self).__init__(*args, **kwargs)
		self.clienteService = ClienteService()
		self.funcionarioService = FuncionarioService()

	def test_criar(self):
		self.login()
		self.criar()
	
	def test_criar_sem_permissao(self):
		self.login_sem_permissao()
		self.assertRaises(Exception, self.criar)

	def criar(self):
		cliente = Cliente()
		cliente.cpf = self.criarStringAleatoria(14)
		self.clienteService.criar(cliente)

	def test_criar_falha(self):
		self.login()
		cliente = Cliente()
		cliente.cpf = self.criarStringAleatoria(14)

		self.clienteService.criar(cliente)
		self.assertRaises(Exception, lambda: self.clienteService.criar(cliente))

	def test_atualizar(self):
		self.login()
		self.atualizar()
	
	def test_atualizar_sem_permissao(self):
		self.login_sem_permissao()
		self.atualizar()

	def atualizar(self):
		self.login()
		cliente = Cliente()
		cliente.cpf = self.criarStringAleatoria(14)
		self.clienteService.criar(cliente)
		self.clienteService.atualizar(cliente)

	def test_listar(self):
		clientes = self.clienteService.listar()
		self.assertIsInstance(clientes, list)

	def test_listar_id(self):
		self.login()
		cliente = Cliente()
		cliente.cpf = self.criarStringAleatoria(14)
		cliente.id = self.clienteService.criar(cliente)

		clientes = self.clienteService.listar(id=cliente.id)
		self.assertIsInstance(clientes, Cliente)
	
	def test_deletar(self):
		self.login()
		self.deletar()

	def test_deletar_sem_permissao(self):
		self.login_sem_permissao()
		self.assertRaises(Exception, self.deletar)

	def deletar(self):
		cliente = Cliente()
		cliente.cpf = self.criarStringAleatoria(14)
		cliente.id = self.clienteService.criar(cliente)
		self.clienteService.deletar(cliente)

	def login(self):
		self.funcionarioService.logout()
		self.funcionarioService.login("366.667.700-20", "12345")

	def login_sem_permissao(self):
		self.funcionarioService.logout()
		self.funcionarioService.login("366.667.700-19", "12345")

	def criarStringAleatoria(self, tamanho):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))