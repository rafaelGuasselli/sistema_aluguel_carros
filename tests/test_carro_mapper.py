import random
import string
import unittest
from model.carro import Carro
from model.carro_mapper import CarroMapper

class TestCarroMapper(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestCarroMapper, self).__init__(*args, **kwargs)
		self.carroMapper = CarroMapper()

	def test(self):
		print("Hello test!")
		print()

	def test_select(self):
		carros = self.carroMapper.listar()
		self.assertIsInstance(carros, list)
		if len(carros) > 0:
			self.assertIsInstance(carros[0], Carro)

	def test_insert(self):
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)

		carro.id = self.carroMapper.criar(carro)
		carroNoBanco = self.carroMapper.listarWhereId(id=carro.id)
		 
		self.assertEqual(carro.placa, carroNoBanco.placa)

	def test_update(self):
		carro = Carro()

		carro.placa = self.criarStringAleatoria(7)
		carro.id = self.carroMapper.criar(carro)

		carro.placa = self.criarStringAleatoria(7)
		self.carroMapper.atualizar(carro)
		
		carroNoBanco = self.carroMapper.listarWhereId(id=carro.id)
		self.assertEqual(carro.placa, carroNoBanco.placa)

	def test_delete(self):
		carro = Carro()
		carro.placa = self.criarStringAleatoria(7)

		carro.id = self.carroMapper.criar(carro)
		self.carroMapper.deletar(id=carro.id)
		
		carro = self.carroMapper.listarWhereId(id=carro.id)
		self.assertEqual(carro, None)
		

	def criarStringAleatoria(self, tamanho):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))