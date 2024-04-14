import random
import string
import unittest
from model.carro import Carro
from model.carro_service import CarroService


class TestCarroService(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestCarroService, self).__init__(*args, **kwargs)
		self.carroService = CarroService()

	def test_criar(self):
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)
		self.carroService.criar(carro)
	
	def test_criar_falha(self):
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)

		self.carroService.criar(carro)
		self.assertRaises(Exception, lambda: self.carroService.criar(carro))

	def test_atualizar(self):
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)
		self.carroService.criar(carro)
		self.carroService.atualizar(carro)

	def test_listar(self):
		carros = self.carroService.listar()
		self.assertIsInstance(carros, list)

	def test_listar_id(self):
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)
		carro.id = self.carroService.criar(carro)

		carros = self.carroService.listar(id=carro.id)
		self.assertIsInstance(carros, Carro)
	
	def test_deletar(self):
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)
		carro.id = self.carroService.criar(carro)
		print(carro.id)

		self.carroService.deletar(carro)

	def criarStringAleatoria(self, tamanho):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))