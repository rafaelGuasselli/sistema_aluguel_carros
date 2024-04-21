import unittest
import random
import string
from src.model.funcionario import Funcionario
from src.model.funcionario_mapper import FuncionarioMapper

class TestFuncionarioMapper(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestFuncionarioMapper, self).__init__(*args, **kwargs)
		self.funcionarioMapper = FuncionarioMapper()

	def test_select(self):
		funcionarios = self.funcionarioMapper.listar()
		self.assertIsInstance(funcionarios, list)
		if len(funcionarios) > 0:
			self.assertIsInstance(funcionarios[0], Funcionario)

	def test_insert(self):
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(11)

		funcionario.id = self.funcionarioMapper.criar(funcionario)

		funcionarioNoBanco = self.funcionarioMapper.listarId(id=funcionario.id)
		self.assertEqual(funcionario.cpf, funcionarioNoBanco.cpf)

	def test_update(self):
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(11)

		funcionario.id = self.funcionarioMapper.criar(funcionario)
		funcionario.cpf = self.criarStringAleatoria(11)

		self.funcionarioMapper.atualizar(funcionario)

		funcionarioNoBanco = self.funcionarioMapper.listarId(funcionario=funcionario)
		self.assertEqual(funcionario.cpf, funcionarioNoBanco.cpf)

	def test_delete(self):
		funcionario = Funcionario()
		funcionario.cpf = self.criarStringAleatoria(11)

		funcionario.id = self.funcionarioMapper.criar(funcionario)
		self.funcionarioMapper.deletar(id=funcionario.id)

		funcionario = self.funcionarioMapper.listarId(id=funcionario.id)
		self.assertEqual(funcionario, None)

	def criarStringAleatoria(self, tamanho):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))