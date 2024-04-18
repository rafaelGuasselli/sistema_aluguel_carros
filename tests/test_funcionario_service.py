import random
import string
import unittest
from model.funcionario import Funcionario
from model.funcionario_service import FuncionarioService


class TestFuncionarioService(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestFuncionarioService, self).__init__(*args, **kwargs)
		self.funcionarioService = FuncionarioService()

	def test_login_aceito(self):
		self.funcionarioService.login("435.402.600-72", "admin")

	def test_criar(self):
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(14)
		self.funcionarioService.criar(funcionario)
	
	def test_criar_falha(self):
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(14)

		self.funcionarioService.criar(funcionario)
		self.assertRaises(Exception, lambda: self.funcionarioService.criar(funcionario))

	def test_atualizar(self):
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(14)
		self.funcionarioService.criar(funcionario)
		self.funcionarioService.atualizar(funcionario)

	def test_listar(self):
		funcionarios = self.funcionarioService.listar()
		self.assertIsInstance(funcionarios, list)

	def test_listar_id(self):
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(14)
		funcionario.id = self.funcionarioService.criar(funcionario)

		funcionarios = self.funcionarioService.listar(id=funcionario.id)
		self.assertIsInstance(funcionarios, Funcionario)
	
	def test_deletar(self):
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(14)
		funcionario.id = self.funcionarioService.criar(funcionario)
		self.funcionarioService.deletar(funcionario)

	def criarStringAleatoria(self, tamanho):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))