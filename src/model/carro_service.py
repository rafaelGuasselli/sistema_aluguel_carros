from .carro import Carro
from .funcionario import Funcionario
from .carro_mapper import CarroMapper
from .funcionario_service import FuncionarioService

class CarroService:
	def __init__(self):
		self.carroMapper = CarroMapper()
		self.funcionarioService = FuncionarioService()
	
	def criar(self, carro):
		try:
			return self.__criar(carro)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao adicionar carro no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __criar(self, carro):
		funcionarioAtual = self.funcionarioService.usuarioAtual()
		naoTemPermissao = not funcionarioAtual.podeAlterarCarros()
		naoEstaLogado = not self.funcionarioService.estaLogado()
		if (naoEstaLogado or naoTemPermissao):
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
		funcionarioAtual = self.funcionarioService.usuarioAtual()
		naoTemPermissao = not funcionarioAtual.podeAlugar() and not funcionarioAtual.podeAlterarCarros()
		naoEstaLogado = not self.funcionarioService.estaLogado()
		if (naoEstaLogado or naoTemPermissao):
			raise Exception("Funcionario não tem permissão de alterar carros!")
		return self.carroMapper.atualizar(carro)

	def listar(self, id=None, carro=None):
		try:
			return self.__listar(id=id, carro=carro)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao ler carros no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __listar(self, id=None, carro=None):
		carros = []

		if id is None and isinstance(carro, Carro): id = carro.id
		if id:
			carros = self.carroMapper.listarId(id=id)
		else:
			carros = self.carroMapper.listar()		
		return carros

	def deletar(self, carro):
		try:
			self.__deletar(carro=carro)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao deletar carro no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)
	
	def __deletar(self, carro):
		funcionarioAtual = self.funcionarioService.usuarioAtual()
		naoTemPermissao = not funcionarioAtual.podeAlterarCarros()
		naoEstaLogado = not self.funcionarioService.estaLogado()
		if (naoEstaLogado or naoTemPermissao):
			raise Exception("Funcionario não tem permissão de alterar carros!")
		self.carroMapper.deletar(id=carro.id)