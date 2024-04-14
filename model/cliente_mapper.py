from .cliente import Cliente
from .sql_mapper import SqlMapper

class ClienteMapper(SqlMapper):
	def __init__(self):
		super(ClienteMapper, self).__init__()
	
	def criar(self, cliente):
		sql = "INSERT INTO Clientes(cpf, nome) VALUES (?,?);"
		values = (cliente.cpf, cliente.nome)
		return super().insert(sql, values)
	
	def atualizar(self, cliente):
		sql = "UPDATE Clientes SET cpf = ?, nome = ? WHERE id = ?;"
		values = (cliente.cpf, cliente.nome, cliente.id)
		return super().update(sql, values)
		
	def listar(self):
		sql = "SELECT id, cpf, nome FROM Clientes;"
		values = ()
		fields = ("id", "cpf", "nome")
		return super().select(sql, values, fields, Cliente)
	
	def listarWhereId(self, id=0, cliente=Cliente()):
		sql = "SELECT id, cpf, nome FROM Clientes WHERE id = ?;"
		values = (id or cliente.id,)
		fields = ("id", "cpf", "nome")
		clientes = super().select(sql, values, fields, Cliente)
		return None if len(clientes) == 0 else clientes[0]
	
	def listarWhereCpf(self, cpf="", cliente=Cliente()):
		sql = "SELECT id, cpf, nome FROM Clientes WHERE cpf = ?;"
		values = (cpf or cliente.cpf,)
		fields = ("id", "cpf", "nome")
		clientes = super().select(sql, values, fields, Cliente)
		return None if len(clientes) == 0 else clientes[0]

	def deletar(self, id=0,cliente=Cliente()):
		sql = "DELETE FROM Clientes WHERE id = ?;"
		values = (id or cliente.id,)
		return super().delete(sql, values)