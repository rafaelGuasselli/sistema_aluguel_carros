import unittest
from src.model.funcionario import Funcionario

class TestFuncionario(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestFuncionario, self).__init__(*args, **kwargs)

	def test_nenhuma_permissao(self):
		funcionario = Funcionario()
		self.assertFalse(funcionario.podeAlterarFuncionarios())
		self.assertFalse(funcionario.podeAlterarCarros())
		self.assertFalse(funcionario.podeAlterarClientes())

	def test_aluguel(self):
		funcionario = Funcionario()
		funcionario.permissoes = 1
		self.assertFalse(funcionario.podeAlterarFuncionarios())
		self.assertFalse(funcionario.podeAlterarCarros())
		self.assertTrue(funcionario.podeAlterarClientes())

	def test_carros(self):
		funcionario = Funcionario()
		funcionario.permissoes = 2
		self.assertFalse(funcionario.podeAlterarFuncionarios())
		self.assertTrue(funcionario.podeAlterarCarros())
		self.assertFalse(funcionario.podeAlterarClientes())

	def test_funcionarios(self):
		funcionario = Funcionario()
		funcionario.permissoes = 4
		self.assertTrue(funcionario.podeAlterarFuncionarios())
		self.assertFalse(funcionario.podeAlterarCarros())
		self.assertFalse(funcionario.podeAlterarClientes())

	def test_tudo(self):
		funcionario = Funcionario()
		funcionario.permissoes = 7
		self.assertTrue(funcionario.podeAlterarFuncionarios())
		self.assertTrue(funcionario.podeAlterarCarros())
		self.assertTrue(funcionario.podeAlterarClientes())