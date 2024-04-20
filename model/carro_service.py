from model.funcionario import Funcionario
from model.carro_mapper import CarroMapper
from model.cache_mapper import CacheMapper
from model.funcionario_mapper import FuncionarioMapper

class CarroService:
	def __init__(self):
		self.carroMapper = CarroMapper()
		self.cacheMapper = CacheMapper()
	
	def criar(self, carro):
		try:
			return self.__criar(carro)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao adicionar carro no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __criar(self, carro):
		funcionarioAtual = self.cacheMapper.listar() or Funcionario()
		if (funcionarioAtual.podeAlterarCarros() is False):
			raise Exception("Funcionario não tem permissão de alterar carros!")
		
		return self.carroMapper.criar(carro)
		

	def atualizar(self, carro):
		try:
			return self.__atualizar(carro)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao atualizar carro no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)
	
	def __atualizar(self, carro):
		funcionarioAtual = self.cacheMapper.listar() or Funcionario()
		if (funcionarioAtual.podeAlterarCarros() is False):
			raise Exception("Funcionario não tem permissão de alterar carros!")
		return self.carroMapper.atualizar(carro)

	def listar(self, id=0, carro=None):
		try:
			return self.__listar(id, carro)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao ler carros no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __listar(self, id=0, carro=None):
		carros = False
		if id or carro:
			carros = self.carroMapper.listarId(id=id,carro=carro)
		else:
			carros = self.carroMapper.listar()		
		return carros

	def deletar(self, carro):
		try:
			self.carroMapper.deletar(carro=carro)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao deletar carro no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)
	
	def __deletar(self, carro):
		funcionarioAtual = self.cacheMapper.listar() or Funcionario()
		if (funcionarioAtual.podeAlterarCarros() is False):
			raise Exception("Funcionario não tem permissão de alterar carros!")
		self.carroMapper.deletar(carro=carro)