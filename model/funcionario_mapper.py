from .funcionario import Funcionario
from .sql_mapper import SqlMapper

class FuncionarioMapper(SqlMapper):
	def __init__(self):
		super(FuncionarioMapper, self).__init__()
	
	def criar(self, funcionario):
		sql = "INSERT INTO Funcionarios(cpf, nome, permissoes) VALUES (?,?,?);"
		values = (funcionario.cpf, funcionario.nome, funcionario.permissoes)
		return super().insert(sql, values)
	
	def atualizar(self, funcionario):
		sql = "UPDATE Funcionarios SET cpf = ?, nome = ?, permissoes = ? WHERE id = ?;"
		values = (funcionario.cpf, funcionario.nome, funcionario.permissoes, funcionario.id)
		return super().update(sql, values)
		
	def listar(self):
		sql = "SELECT id, cpf, nome, permissoes FROM Funcionarios;"
		values = ()
		fields = ("id", "cpf", "nome", "permissoes")
		return super().select(sql, values, fields, Funcionario)

	def listarWhereId(self, id=0, funcionario=Funcionario()):
		sql = "SELECT id, cpf, nome, permissoes FROM Funcionarios WHERE id = ?;"
		values = (id or funcionario.id,)
		fields = ("id", "cpf", "nome", "permissoes")
		funcionarios = super().select(sql, values, fields, Funcionario)
		return None if len(funcionarios) == 0 else funcionarios[0]

	def deletar(self, id=0,funcionario=Funcionario()):
		sql = "DELETE FROM Funcionarios WHERE id = ?;"
		values = (id or funcionario.id,)
		return super().delete(sql, values)