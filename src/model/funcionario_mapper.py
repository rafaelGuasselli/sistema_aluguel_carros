from .funcionario import Funcionario
from .sql_mapper import SqlMapper

class FuncionarioMapper(SqlMapper):
	def __init__(self):
		super(FuncionarioMapper, self).__init__()
	
	def criar(self, funcionario):
		sql = "INSERT INTO Funcionarios(nome, permissoes) VALUES (?,?);"
		values = (funcionario.nome, funcionario.permissoes)
		return super()._insert(sql, values)
	
	def atualizar(self, funcionario):
		sql = "UPDATE Funcionarios SET nome = ?, permissoes = ? WHERE id = ?;"
		values = (funcionario.nome, funcionario.permissoes, funcionario.id)
		return super()._update(sql, values)
		
	def listar(self):
		sql = "SELECT id, nome, permissoes FROM Funcionarios;"
		values = ()
		fields = ("id", "nome", "permissoes")
		return super()._select(sql, values, fields, Funcionario)

	def listarId(self, id=None):
		sql = "SELECT id, nome, permissoes FROM Funcionarios WHERE id = ?;"
		values = (id,)
		fields = ("id", "nome", "permissoes")
		funcionarios = super()._select(sql, values, fields, Funcionario)
		return None if len(funcionarios) == 0 else funcionarios[0]

	def listarNomeSenha(self, nome=None, senha=None):
		sql = "SELECT id, nome, permissoes FROM Funcionarios WHERE nome = ? and hash_senha = ?;"
		values = (nome, senha)
		fields = ("id", "nome", "permissoes")
		funcionarios = super()._select(sql, values, fields, Funcionario)
		return None if len(funcionarios) == 0 else funcionarios[0]

	def deletar(self, id=None):
		sql = "DELETE FROM Funcionarios WHERE id = ?;"
		values = (id,)
		super()._delete(sql, values)