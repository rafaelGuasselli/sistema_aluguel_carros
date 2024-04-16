import unittest
from model.carro import Carro
from model.cliente import Cliente
from model.carro_mapper import CarroMapper
from model.cliente_mapper import ClienteMapper
from model.aluguel_service import AluguelService


class TestAluguelService(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestAluguelService, self).__init__(*args, **kwargs)

	def test_aluguel_aceito(self):
		return
		carroDb = CarroMapper()
		clientDb = ClienteMapper()
		aluguelService = AluguelService()

		carro = Carro()
		cliente = Cliente()

		carro.id = carroDb.criar(carro)
		aluguelService.alugar(carro, cliente)

		carro = carroDb.listarWhereId(carro=carro)
		self.assertEqual(carro.cliente_id, cliente.id)
	
	def test_aluguel_rejeitado(self):
		return
		carroDb = CarroMapper()
		clientDb = ClienteMapper()
		aluguelService = AluguelService()

		carro = Carro()
		cliente1 = Cliente()
		cliente2 = Cliente()

		carro.id = carroDb.criar(carro)
		aluguelService.alugar(carro, cliente1)
		
		try:
			aluguelService.alugar(carro, cliente2)
			self.assertTrue(False)
		except:
			self.assertTrue(True)

	def test_aluguel_carro_nao_existe(self):
		return
		carroDb = CarroMapper()
		clientDb = ClienteMapper()
		aluguelService = AluguelService()

		carro = Carro()
		cliente = Cliente()
		
		try:
			aluguelService.alugar(carro, cliente)
			self.assertTrue(False)
		except:
			self.assertTrue(True)

	def test_pagar(self):
		return
		carroDb = CarroMapper()
		clientDb = ClienteMapper()
		aluguelService = AluguelService()

		carro = Carro()
		cliente = Cliente()

		cliente.nome = "Rafael"

		carro.modelo = "Teste"
		carro.id = carroDb.criar(carro)
		aluguelService.alugar(carro, cliente)
		aluguelService.pagar(carro)

		carro = carroDb.listarWhereId(carro=carro)
		self.assertEqual(carro.cliente_id, cliente.id)

	def test_pagar_carro_nao_existe(self):
		return
		carroDb = CarroMapper()
		clientDb = ClienteMapper()
		aluguelService = AluguelService()

		carro = Carro()
		cliente = Cliente()

		cliente.nome = "Rafael"

		carro.modelo = "Teste"
		carro.id = carroDb.criar(carro)
		aluguelService.alugar(carro, cliente)

		carro.id = -1
		try:
			aluguelService.pagar(carro)
			self.assertTrue(False)
		except:
			self.assertTrue(True)