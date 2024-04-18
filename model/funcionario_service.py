from model.funcionario_mapper import FuncionarioMapper
import hashlib, uuid

class FuncionarioService:
	def __init__(self):
		self.funcionarioMapper = FuncionarioMapper()
	
	def login(self, cpf, senha):
		try:
			return self.__login(cpf, senha)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao logar!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __login(self, cpf, senha):
		salt = uuid.uuid4().hex
		senha_hash = hashlib.sha512(bytes(senha, 'utf-8')).hexdigest()
		funcionario = self.funcionarioMapper.listarCpfSenha(cpf, senha_hash)
		
		if funcionario is None:
			raise Exception("Usuário ou senha incorretos!")

		return funcionario

	def criar(self, funcionario):
		funcionario.senha = hashlib.sha512(bytes(funcionario.senha, 'utf-8')).hexdigest()
		return self.__criar(funcionario)

	def __criar(self, funcionario):
		try:
			return self.funcionarioMapper.criar(funcionario)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao adicionar funcionario no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)

	def atualizar(self, funcionario):
		try:
			return self.funcionarioMapper.atualizar(funcionario)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao atualizar funcionario no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)

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
			return self.funcionarioMapper.deletar(funcionario=funcionario)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao deletar funcionario no banco de dados!\n{}".format(detalhes)
			raise Exception(mensagem)
