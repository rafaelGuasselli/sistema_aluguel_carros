from model.funcionario_mapper import FuncionarioMapper

class FuncionarioService:
	def __init__(self):
		self.funcionarioMapper = FuncionarioMapper()
	
	def criar(self, funcionario):
		funcionarioId = self.funcionarioMapper.criar(funcionario)
		if not funcionarioId:
			raise Exception("Falha ao adicionar funcionario no banco de dados!")
		return funcionarioId

	def atualizar(self, funcionario):
		atualizado = self.funcionarioMapper.atualizar(funcionario)
		if not atualizado:
			raise Exception("Falha ao atualizar funcionario no banco de dados!")

	def listar(self, id=0, funcionario=None):
		funcionarios = False
		if id or funcionario:
			funcionarios = self.funcionarioMapper.listarWhereId(id=id,funcionario=funcionario)
		else:
			funcionarios = self.funcionarioMapper.listar()
		
		if not funcionarios:
			raise Exception("Falha ao ler funcionarios no banco de dados!")
		
		return funcionarios

	def deletar(self, funcionario):
		deletado = self.funcionarioMapper.deletar(funcionario=funcionario)
		if not deletado:
			raise Exception("Falha ao deletar funcionario no banco de dados!")
