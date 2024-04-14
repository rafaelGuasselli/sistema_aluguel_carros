import unittest
from model.funcionario_mapper import FuncionarioMapper
from model.funcionario import Funcionario

class TestFuncionarioMapper(unittest.TestCase):
	def test_select(self):
		funcionarioDB = FuncionarioMapper()
		funcionarios = funcionarioDB.listar()
		self.assertTrue(type(funcionarios) == list)

		count = 0
		print()
		for funcionario in funcionarios:
			if count == 1:
				break
			print("------------")
			print(funcionario.cpf)
			print(funcionario.nome)
			print(funcionario.permissoes)
			print("-------------")
			count += 1
		print()

	def test_insert(self):
		funcionarioDB = FuncionarioMapper()
		funcionario = Funcionario()
		funcionario.nome = "a"

		funcionarioId = funcionarioDB.criar(funcionario)
		self.assertTrue(funcionarioId)

		funcionarioNoBanco = funcionarioDB.listarWhereId(id=funcionarioId)
		self.assertEqual(funcionario.nome, funcionarioNoBanco.nome)

	def test_update(self):
		funcionarioDB = FuncionarioMapper()
		funcionario = Funcionario()
		funcionario.nome = "A" 

		funcionarioId = funcionarioDB.criar(funcionario)
		
		funcionario.id = funcionarioId
		funcionario.nome = "B"

		funcionarioDB.atualizar(funcionario)

		funcionarioNoBanco = funcionarioDB.listarWhereId(funcionario=funcionario)
		self.assertEqual(funcionario.nome, funcionarioNoBanco.nome)

	def test_delete(self):
		funcionarioDB = FuncionarioMapper()
		funcionario = Funcionario()

		funcionarioId = funcionarioDB.criar(funcionario)
		self.assertTrue(funcionarioId)

		funcionarioDB.deletar(id=funcionarioId)

		funcionario = funcionarioDB.listarWhereId(id=funcionarioId)
		self.assertEqual(funcionario, None)