import unittest
from model.carro_mapper import CarroMapper
from model.carro import Carro

class TestCarroMapper(unittest.TestCase):
	def test(self):
		print("Hello test!")
		print()

	def test_select(self):
		carroDB = CarroMapper()
		carros = carroDB.listar()
		self.assertTrue(type(carros) == list)

		count = 0
		print()
		for carro in carros:
			if count == 1:
				break
			print("------------")
			print(carro.cor)
			print(carro.modelo)
			print(carro.taxa_dia)
			print("-------------")
			count += 1
		print()

	def test_insert(self):
		carroDB = CarroMapper()
		carro = Carro()
		carro.modelo = "Prius"
		carro.cor = "Vermelho"
		carro.multa = 50
		carro.placa = "abc123"
		carro.taxa_dia = 200
		carro.estimativa_devolucao = None

		carroId = carroDB.criar(carro)
		self.assertTrue(carroId)

		carro2 = carroDB.listarWhereId(id=carroId)
		self.assertEqual(carro.modelo, carro2.modelo)

		#Remover influencia no bd
		carroDB.deletar(id=carroId)

	def test_update(self):
		carroDB = CarroMapper()
		carro = Carro()
		carro.modelo = "A"

		carroId = carroDB.criar(carro)
		
		carro.id = carroId
		carro.modelo = "B"

		carroDB.atualizar(carro)

		carroNoBanco = carroDB.listarWhereId(carro=carro)
		self.assertEqual(carro.modelo, carroNoBanco.modelo)
		

		#Remover influencia no bd
		carroDB.deletar(carro=carro)

	def test_delete(self):
		carroDB = CarroMapper()
		carro = Carro()

		carroId = carroDB.criar(carro)
		self.assertTrue(carroId)

		carroDB.deletar(id=carroId)

		carro = carroDB.listarWhereId(id=carroId)
		self.assertEqual(carro, None)
		

if __name__ == '__main__':
	unittest.main()