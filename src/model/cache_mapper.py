from .funcionario import Funcionario
from .sql_mapper import SqlMapper

class CacheMapper(SqlMapper):
	def __init__(self):
		super(CacheMapper, self).__init__()

	def criar(self, id=None, funcionario=None):
		sql = "INSERT INTO Cache(funcionario_atual) VALUES (?);"
		values = (id or funcionario.id,)
		return super()._insert(sql, values)	
	
	def listar(self):
		sql = "SELECT funcionario_atual as id, nome, cpf, permissoes FROM Cache INNER JOIN Funcionarios funcionario ON (funcionario.id = funcionario_atual);"
		values = ()
		fields = ("id", "nome", "cpf", "permissoes")
		funcionarios = super()._select(sql, values, fields, Funcionario)
		return None if len(funcionarios) == 0 else funcionarios[0]

	def deletar(self):
		sql = "DELETE FROM Cache WHERE id = 1;"
		values = ()
		super()._delete(sql, values)