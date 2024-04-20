import random
import string
import unittest
from model.carro import Carro
from model.carro_service import CarroService
from model.funcionario_service import FuncionarioService


class TestCarroService(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestCarroService, self).__init__(*args, **kwargs)
		self.carroService = CarroService()
		self.funcionarioService = FuncionarioService()

	def test_criar(self):
		self.login()
		self.criar()

	def test_criar_sem_permissao(self):
		self.login_sem_permissao()
		self.assertRaises(Exception, self.criar)

	def criar(self):
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)
		self.carroService.criar(carro)
	
	def test_criar_falha(self):
		self.login()
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)

		self.carroService.criar(carro)
		self.assertRaises(Exception, lambda: self.carroService.criar(carro))

	def test_atualizar(self):
		self.login()
		self.atualizar()

	def test_atualizar_sem_permissao(self):
		self.login_sem_permissao()
		self.assertRaises(Exception, self.atualizar)

	def atualizar(self):
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)
		self.carroService.criar(carro)
		self.carroService.atualizar(carro)

	def test_listar(self):
		self.login()
		carros = self.carroService.listar()
		self.assertIsInstance(carros, list)

	def test_listar_id(self):
		self.login()
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)
		carro.id = self.carroService.criar(carro)

		carros = self.carroService.listar(id=carro.id)
		self.assertIsInstance(carros, Carro)
	

	def test_deletar(self):
		self.login()
		self.deletar()
	
	def test_deletar_sem_permissao(self):
		self.login_sem_permissao()
		self.assertRaises(Exception, self.deletar)

	def deletar(self):
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)
		carro.id = self.carroService.criar(carro)
		self.carroService.deletar(carro)

	def login(self):
		self.funcionarioService.logout()
		self.funcionarioService.login("366.667.700-21", "12345")

	def login_sem_permissao(self):
		self.funcionarioService.logout()
		self.funcionarioService.login("366.667.700-20", "12345")


	def criarStringAleatoria(self, tamanho):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))