import unittest
from model.cliente_mapper import ClienteMapper
from model.cliente import Cliente

class TestClienteMapper(unittest.TestCase):
	def test_select(self):
		clienteDB = ClienteMapper()
		clientes = clienteDB.listar()
		self.assertTrue(type(clientes) == list)

		count = 0
		print()
		for cliente in clientes:
			if count == 1:
				break
			print("------------")
			print(cliente.cpf)
			print(cliente.nome)
			print("-------------")
			count += 1
		print()

	def test_insert(self):
		clienteDB = ClienteMapper()
		cliente = Cliente()
		cliente.nome = "a"

		clienteId = clienteDB.criar(cliente)
		self.assertTrue(clienteId)

		clienteNoBanco = clienteDB.listarWhereId(id=clienteId)
		self.assertEqual(cliente.nome, clienteNoBanco.nome)

		#Remover influencia no bd
		clienteDB.deletar(id=clienteId)

	def test_update(self):
		clienteDB = ClienteMapper()
		cliente = Cliente()
		cliente.modelo = "A" 

		clienteId = clienteDB.criar(cliente)
		
		cliente.id = clienteId
		cliente.modelo = "B"

		clienteDB.atualizar(cliente)

		clienteNoBanco = clienteDB.listarWhereId(cliente=cliente)
		self.assertEqual(cliente.nome, clienteNoBanco.nome)
		

		#Remover influencia no bd
		clienteDB.deletar(cliente=cliente)

	def test_delete(self):
		clienteDB = ClienteMapper()
		cliente = Cliente()

		clienteId = clienteDB.criar(cliente)
		self.assertTrue(clienteId)

		clienteDB.deletar(id=clienteId)

		cliente = clienteDB.listarWhereId(id=clienteId)
		self.assertEqual(cliente, None)
		

if __name__ == '__main__':
	unittest.main()