import random
import string
import unittest
from model.cliente import Cliente
from model.cliente_service import ClienteService
from model.funcionario_service import FuncionarioService

class TestClienteService(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestClienteService, self).__init__(*args, **kwargs)
		self.clienteService = ClienteService()
		self.funcionarioService = FuncionarioService()

	def login(self):
		self.funcionarioService.logout()
		self.funcionarioService.login("435.402.600-72", "admin")

	def test_criar(self):
		self.login()
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
		cliente = Cliente()
		cliente.cpf = self.criarStringAleatoria(14)
		cliente.id = self.clienteService.criar(cliente)
		self.clienteService.deletar(cliente)

	def criarStringAleatoria(self, tamanho):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))