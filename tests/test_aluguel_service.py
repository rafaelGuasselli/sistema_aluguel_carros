import unittest
import random
import string
from model.carro import Carro
from model.cliente import Cliente
from model.carro_service import CarroService
from model.cliente_service import ClienteService
from model.aluguel_service import AluguelService
from model.funcionario_service import FuncionarioService


class TestAluguelService(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestAluguelService, self).__init__(*args, **kwargs)
		self.carroService = CarroService()
		self.clienteService = ClienteService()
		self.aluguelService = AluguelService()
		self.funcionarioService = FuncionarioService()

	def login(self):
		self.funcionarioService.logout()
		self.funcionarioService.login("435.402.600-72", "admin")

	def test_aluguel_aceito(self):
		self.login()
		carro = Carro()
		cliente = Cliente()
		carro.placa = self.criarStringAleatoria(7)
		cliente.cpf = self.criarStringAleatoria(11)

		carro.id = self.carroService.criar(carro)
		self.aluguelService.alugar(carro, cliente)

		carro = self.carroService.listar(carro=carro)
		self.assertEqual(carro.cliente_id, cliente.id)
	
	def test_aluguel_rejeitado(self):
		self.login()
		carro = Carro()
		cliente1 = Cliente()
		cliente2 = Cliente()
		
		carro.placa = self.criarStringAleatoria(7)
		cliente1.cpf = self.criarStringAleatoria(11)
		cliente2.cpf = self.criarStringAleatoria(11)	

		carro.id = self.carroService.criar(carro)
		self.aluguelService.alugar(carro, cliente1)
		
		try:
			self.aluguelService.alugar(carro, cliente2)
			self.assertTrue(False)
		except:
			self.assertTrue(True)

	def test_aluguel_carro_nao_existe(self):
		self.login()
		carro = Carro()
		cliente = Cliente()
		
		try:
			self.aluguelService.alugar(carro, cliente)
			self.assertTrue(False)
		except:
			self.assertTrue(True)

	def test_pagar(self):
		self.login()
		carro = Carro()
		cliente = Cliente()

		carro.placa = self.criarStringAleatoria(7)
		cliente.cpf = self.criarStringAleatoria(11)	

		carro.id = self.carroService.criar(carro)
		self.aluguelService.alugar(carro, cliente)
		self.aluguelService.pagar(carro)

		carro = self.carroService.listar(carro=carro)
		self.assertEqual(carro.cliente_id, cliente.id)

	def test_pagar_carro_nao_existe(self):
		self.login()
		carro = Carro()
		cliente = Cliente()
		carro.id = -1
		
		try:
			self.aluguelService.pagar(carro)
			self.assertTrue(False)
		except:
			self.assertTrue(True)
	
	def criarStringAleatoria(self, tamanho):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))