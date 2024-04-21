import random
import string
import unittest
from src.model.funcionario import Funcionario
from src.model.funcionario_service import FuncionarioService

class TestFuncionarioService(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestFuncionarioService, self).__init__(*args, **kwargs)
		self.funcionarioService = FuncionarioService()

	def test_login_aceito(self):
		self.funcionarioService.logout()
		self.funcionarioService.login("435.402.600-72", "admin")

	def test_login_rejeitado(self):
		self.funcionarioService.logout()
		self.assertRaises(Exception, lambda: self.funcionarioService.login("435.402.600-72", ""))
	
	def test_login_ja_logado(self):
		self.funcionarioService.logout()
		self.funcionarioService.login("435.402.600-72", "admin")
		self.assertRaises(Exception, lambda:self.funcionarioService.login("435.402.600-72", "admin"))

	def test_logout(self):
		self.login()
		self.funcionarioService.logout()
		self.funcionarioService.logout()

	def test_criar(self):
		self.login()
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(14)
		self.funcionarioService.criar(funcionario)
	
	def test_criar_sem_permissao(self):
		self.login_sem_permissao()
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(14)
		self.assertRaises(Exception, lambda: self.funcionarioService.criar(funcionario))

	def test_criar_falha(self):
		self.login()
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(14)

		self.funcionarioService.criar(funcionario)
		self.assertRaises(Exception, lambda: self.funcionarioService.criar(funcionario))

	def test_atualizar(self):
		self.login()
		self.atualizar()

	def test_atualizar_sem_permissao(self):
		self.login_sem_permissao()
		self.assertRaises(Exception, self.atualizar)

	def atualizar(self):
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(14)
		self.funcionarioService.criar(funcionario)
		self.funcionarioService.atualizar(funcionario)

	def test_listar(self):
		self.login()
		funcionarios = self.funcionarioService.listar()
		self.assertIsInstance(funcionarios, list)

	def test_listar_id(self):
		self.login()
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(14)
		funcionario.id = self.funcionarioService.criar(funcionario)

		funcionarios = self.funcionarioService.listar(id=funcionario.id)
		self.assertIsInstance(funcionarios, Funcionario)
	
	def test_deletar(self):
		self.login()
		self.deletar()

	def test_deletar_sem_permissao(self):
		self.login_sem_permissao()
		self.assertRaises(Exception, self.deletar)

	def deletar(self):
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(14)
		funcionario.id = self.funcionarioService.criar(funcionario)
		self.funcionarioService.deletar(funcionario)

	def login(self):
		self.funcionarioService.logout()
		self.funcionarioService.login("435.402.600-72", "admin")

	def login_sem_permissao(self):
		self.funcionarioService.logout()
		self.funcionarioService.login("366.667.700-19", "12345")

	def criarStringAleatoria(self, tamanho):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))