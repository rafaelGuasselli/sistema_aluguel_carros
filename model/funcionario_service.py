import hashlib, uuid
from model.funcionario import Funcionario
from model.cache_mapper import CacheMapper
from model.funcionario_mapper import FuncionarioMapper


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
		if self.cacheMapper.listar() != None:
			raise Exception("Você já está logado!")

		#salt = uuid.uuid4().hex
		#Com o salt não tem como comparar direto no bd sem carregar a senha na memoria.
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
		funcionarioAtual = self.cacheMapper.listar() or Funcionario()
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
		funcionarioAtual = self.cacheMapper.listar() or Funcionario()
		if (funcionarioAtual.podeAlterarFuncionarios() is False):
			raise Exception("Funcionario não tem permissão de alterar funcionarios!")

		return self.funcionarioMapper.atualizar(funcionario)

	def listar(self, id=0, funcionario=None):
		try:
			return self.__listar(id, funcionario)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao ler funcionarios no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)
	
	def __listar(self, id=0, funcionario=None):
		funcionarios = False
		if id or funcionario:
			funcionarios = self.funcionarioMapper.listarId(id=id,funcionario=funcionario)
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
		funcionarioAtual = self.cacheMapper.listar() or Funcionario()
		if (funcionarioAtual.podeAlterarFuncionarios() is False):
			raise Exception("Funcionario não tem permissão de alterar funcionarios!")

		return self.funcionarioMapper.deletar(funcionario=funcionario)