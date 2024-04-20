from model.cliente_mapper import ClienteMapper
from model.cache_mapper import CacheMapper
from model.funcionario import Funcionario

class ClienteService:
	def __init__(self):
		self.clienteMapper = ClienteMapper()
		self.cacheMapper = CacheMapper()
	
	def criar(self, cliente):
		try:
			return self.__criar(cliente)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao adicionar cliente no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)
	
	def __criar(self, cliente):
		funcionarioAtual = self.cacheMapper.listar() or Funcionario()
		if (funcionarioAtual.podeAlterarClientes() is False):
			raise Exception("Funcionario não tem permissão de alterar clientes!")

		return self.clienteMapper.criar(cliente)

	def atualizar(self, cliente):
		try:
			return self.__atualizar(cliente)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao atualizar cliente no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __atualizar(self, cliente):
		funcionarioAtual = self.cacheMapper.listar() or Funcionario()
		if (funcionarioAtual.podeAlterarClientes() is False):
			raise Exception("Funcionario não tem permissão de alterar clientes!")
		
		return self.clienteMapper.atualizar(cliente)

	def listar(self, id=0, cliente=None):
		try:
			return self.__listar(id, cliente)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao ler cliente no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __listar(self, id=0, cliente=None):
		clientes = False
		if id or cliente:
			clientes = self.clienteMapper.listarId(id=id,cliente=cliente)
		else:
			clientes = self.clienteMapper.listar()
		
		return clientes

	def deletar(self, cliente):
		try:
			self.__deletar(cliente=cliente)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao deletar cliente no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __deletar(self, cliente):
		funcionarioAtual = self.cacheMapper.listar() or Funcionario()
		if (funcionarioAtual.podeAlterarClientes() is False):
			raise Exception("Funcionario não tem permissão de alterar clientes!")
		self.clienteMapper.deletar(cliente=cliente)
