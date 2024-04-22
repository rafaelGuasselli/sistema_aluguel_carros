from .carro import Carro
from .sql_mapper import SqlMapper

class CarroMapper(SqlMapper):
	def __init__(self):
		super(CarroMapper, self).__init__()

	def criar(self, carro):
		sql = "INSERT INTO Carros(cor, taxa_hora, placa, modelo, taxa_dia, data_aluguel) VALUES (?,?,?,?,?,?);"
		values = (carro.cor, carro.taxa_hora, carro.placa, carro.modelo, carro.taxa_dia, carro.data_aluguel)
		return super()._insert(sql, values)	
	
	def atualizar(self, carro):
		sql = "UPDATE Carros SET cor = ?, taxa_hora = ?, placa = ?, modelo = ?, taxa_dia = ?, cliente_id = ?, data_aluguel = ? WHERE id = ?;"
		values = (carro.cor, carro.taxa_hora, carro.placa, carro.modelo, carro.taxa_dia, carro.cliente_id, carro.data_aluguel, carro.id)
		super()._update(sql, values)
		
	def listar(self):
		sql = "SELECT id, cor, taxa_hora, placa, modelo, taxa_dia, cliente_id, data_aluguel FROM Carros;"
		values = ()
		fields = ("id", "cor", "taxa_hora", "placa", "modelo", "taxa_dia", "cliente_id", "data_aluguel")
		return super()._select(sql, values, fields, Carro)
	
	def listarId(self, id=None):
		sql = "SELECT id, cor, taxa_hora, placa, modelo, taxa_dia, cliente_id, data_aluguel FROM Carros WHERE id = ?;"
		values = (id,)
		fields = ("id", "cor", "taxa_hora", "placa", "modelo", "taxa_dia", "cliente_id", "data_aluguel")
		carros = super()._select(sql, values, fields, Carro)
		return None if len(carros) == 0 else carros[0]

	def deletar(self, id=None):
		sql = "DELETE FROM Carros WHERE id = ?;"
		values = (id,)
		super()._delete(sql, values)