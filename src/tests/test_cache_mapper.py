import random
import string
import unittest
from src.model.funcionario import Funcionario
from src.model.cache_mapper import CacheMapper
from src.model.funcionario_service import FuncionarioService

class TestCarroMapper(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestCarroMapper, self).__init__(*args, **kwargs)
		self.cacheMapper = CacheMapper()
		self.funcionarioService = FuncionarioService()
	
	def test_criar_sucesso(self):
		self.login()
		funcionario = Funcionario()
		funcionario.nome = self.criarStringAleatoria(50)
		funcionario.id = self.funcionarioService.criar(funcionario)
		
		self.cacheMapper.deletar()
		self.cacheMapper.criar(funcionario=funcionario)
		funcionarioNoCache = self.cacheMapper.listar()

		self.assertEqual(funcionario.nome, funcionarioNoCache.nome)

	def test_criar_ja_existe(self):
		self.login()
		funcionario = Funcionario()
		funcionario.nome = self.criarStringAleatoria(50)
		funcionario.id = self.funcionarioService.criar(funcionario)
		
		self.cacheMapper.deletar()
		self.cacheMapper.criar(funcionario=funcionario)
		self.assertRaises(Exception, lambda:self.cacheMapper.criar(funcionario=funcionario))

		
	def test_select(self):
		self.login()
		funcionario = Funcionario()
		funcionario.nome = self.criarStringAleatoria(50)
		funcionario.id = self.funcionarioService.criar(funcionario)
		
		self.cacheMapper.deletar()
		self.cacheMapper.criar(funcionario=funcionario)
		funcionarioNoCache = self.cacheMapper.listar()

		self.assertIsInstance(funcionarioNoCache, Funcionario)

	def test_delete(self):
		self.login()
		funcionario = Funcionario()
		funcionario.nome = self.criarStringAleatoria(50)
		funcionario.id = self.funcionarioService.criar(funcionario)
		
		self.cacheMapper.deletar()
		self.cacheMapper.criar(funcionario=funcionario)
		self.cacheMapper.deletar()
		funcionarioNoCache = self.cacheMapper.listar()
		self.assertIsNone(funcionarioNoCache)

	def login(self):
		self.funcionarioService.logout()
		self.funcionarioService.login("admin", "admin")

	def criarStringAleatoria(self, tamanho):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))