import random
import string
import unittest
from model.cliente import Cliente
from model.cliente_mapper import ClienteMapper

class TestClienteMapper(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestClienteMapper, self).__init__(*args, **kwargs)
		self.clienteMapper = ClienteMapper()

	def test_insert(self):
		cliente = Cliente()
		cliente.cpf = self.criarStringAleatoria(14)

		cliente.id = self.clienteMapper.criar(cliente)
		clienteNoBanco = self.clienteMapper.listarId(id=cliente.id)
		self.assertEqual(cliente.nome, clienteNoBanco.nome)

	def test_select(self):
		clientes = self.clienteMapper.listar()
		self.assertIsInstance(clientes, list)
		if len(clientes) > 0:
			self.assertIsInstance(clientes[0], Cliente)

	def test_update(self):
		cliente = Cliente()

		cliente.cpf = self.criarStringAleatoria(14)
		cliente.id = self.clienteMapper.criar(cliente)

		cliente.cpf = self.criarStringAleatoria(14)
		self.clienteMapper.atualizar(cliente)

		clienteNoBanco = self.clienteMapper.listarId(id=cliente.id)
		self.assertEqual(cliente.cpf, clienteNoBanco.cpf)

	def test_delete(self):
		cliente = Cliente()
		cliente.cpf = self.criarStringAleatoria(14)

		cliente.id = self.clienteMapper.criar(cliente)
		self.clienteMapper.deletar(id=cliente.id)

		cliente = self.clienteMapper.listarId(id=cliente.id)
		self.assertEqual(cliente, None) 

	def criarStringAleatoria(self, tamanho):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))