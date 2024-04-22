import hashlib, uuid
from .funcionario import Funcionario
from .cache_mapper import CacheMapper
from .funcionario_mapper import FuncionarioMapper

class FuncionarioService:
	def __init__(self):
		self.funcionarioMapper = FuncionarioMapper()
		self.cacheMapper = CacheMapper()
	
	def login(self, cpf, senha):
		try:
			self.__login(cpf, senha)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao logar!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __login(self, cpf, senha):
		self.logout()
		#salt = uuid.uuid4().hex
		#TODO: Adicionar salt.
		senha_hash = hashlib.sha512(bytes(senha, 'utf-8')).hexdigest()
		funcionario = self.funcionarioMapper.listarCpfSenha(cpf, senha_hash)
		
		if funcionario is None:
			raise Exception("Usuário ou senha incorretos!")

		self.cacheMapper.criar(funcionario=funcionario)

	def logout(self):
		try:
			return self.__logout()
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao deslogar!\n{}".format(detalhes)
			raise Exception(mensagem)
	
	def __logout(self):
		self.cacheMapper.deletar()

	def criar(self, funcionario):
		try:
			return self.__criar(funcionario)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao adicionar funcionario no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __criar(self, funcionario):
		funcionarioAtual = self.usuarioAtual()
		if (funcionarioAtual.podeAlterarFuncionarios() is False):
			raise Exception("Funcionario não tem permissão de alterar funcionarios!")

		funcionario.senha = hashlib.sha512(bytes(funcionario.senha, 'utf-8')).hexdigest()
		return self.funcionarioMapper.criar(funcionario)

	def atualizar(self, funcionario):
		try:
			return self.__atualizar(funcionario)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao atualizar funcionario no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __atualizar(self, funcionario):
		funcionarioAtual = self.usuarioAtual()
		if (funcionarioAtual.podeAlterarFuncionarios() is False):
			raise Exception("Funcionario não tem permissão de alterar funcionarios!")

		return self.funcionarioMapper.atualizar(funcionario)

	def listar(self, id=None, funcionario=None):
		try:
			return self.__listar(id, funcionario)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao ler funcionarios no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)
	
	def __listar(self, id=None, funcionario=None):
		funcionarios = False
		if id is None and isinstance(funcionario, Funcionario): id = funcionario.id
		if id:
			funcionarios = self.funcionarioMapper.listarId(id=id)
		else:
			funcionarios = self.funcionarioMapper.listar()
		
		return funcionarios

	def deletar(self, funcionario):
		try:
			return self.__deletar(funcionario=funcionario)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao deletar funcionario no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)
	
	def __deletar(self, funcionario):
		funcionarioAtual = self.usuarioAtual()
		if (funcionarioAtual.podeAlterarFuncionarios() is False):
			raise Exception("Funcionario não tem permissão de alterar funcionarios!")

		return self.funcionarioMapper.deletar(id=funcionario.id)
	
	def estaLogado(self):
		return self.cacheMapper.listar() != None

	def usuarioAtual(self):
		return self.cacheMapper.listar() or Funcionario()