from model.funcionario_mapper import FuncionarioMapper

class FuncionarioService:
	def __init__(self):
		self.funcionarioMapper = FuncionarioMapper()
	
	def criar(self, funcionario):
		try:
			return self.funcionarioMapper.criar(funcionario)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao adicionar funcionario no banco de dados!\n{detalhes}"
			raise Exception(mensagem)

	def atualizar(self, funcionario):
		try:
			return self.funcionarioMapper.atualizar(funcionario)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao atualizar funcionario no banco de dados!\n{detalhes}"
			raise Exception(mensagem)

	def listar(self, id=0, funcionario=None):
		try:
			return self.__listar(id, funcionario)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao ler funcionarios no banco de dados!\n{detalhes}"
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
			mensagem = "Falha ao deletar funcionario no banco de dados!\n{detalhes}"
			raise Exception(mensagem)
