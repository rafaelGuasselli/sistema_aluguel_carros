from .cliente_mapper import ClienteMapper
from .cache_mapper import CacheMapper
from .funcionario import Funcionario
from model.cliente import Cliente

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

	def listar(self, id=0, cpf="", cliente=None):
		try:
			return self.__listar(id=id, cpf=cpf, cliente=cliente)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao ler cliente no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __listar(self, id=0, cpf=None, cliente=None):
		clientes = False
		if cpf or (cliente and cliente.cpf):
			cpf = cpf or cliente.cpf
			clientes = self.clienteMapper.listarCpf(cpf=cpf)
		elif id or (cliente and cliente.id):
			id = id or cliente.id
			clientes = self.clienteMapper.listarId(id=id)
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
