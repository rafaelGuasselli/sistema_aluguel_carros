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

	def login(self):
		self.funcionarioService.logout()
		self.funcionarioService.login("435.402.600-72", "admin")

	def test_criar(self):
		self.login()
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
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)
		carro.id = self.carroService.criar(carro)
		self.carroService.deletar(carro)

	def criarStringAleatoria(self, tamanho):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))