from .carro import Carro
from .sql_mapper import SqlMapper

class CarroMapper(SqlMapper):
	def __init__(self):
		super(CarroMapper, self).__init__()

	def criar(self, carro):
		sql = "INSERT INTO Carros(cor, multa, placa, modelo, taxa_dia, estimativa_devolucao) VALUES (?,?,?,?,?,?);"
		values = (carro.cor, carro.multa, carro.placa, carro.modelo, carro.taxa_dia, carro.estimativa_devolucao)
		return self.insert(sql, values)	
	
	def atualizar(self, carro):
		sql = "UPDATE Carros SET cor = ?, multa = ?, placa = ?, modelo = ?, taxa_dia = ?, estimativa_devolucao = ? WHERE id = ?;"
		values = (carro.cor, carro.multa, carro.placa, carro.modelo, carro.taxa_dia, carro.estimativa_devolucao, carro.id)
		return self.update(sql, values)
		
	def listar(self):
		sql = "SELECT id, cor, multa, placa, modelo, taxa_dia, estimativa_devolucao FROM Carros;"
		values = ()
		fields = ("id", "cor", "multa", "placa", "modelo", "taxa_dia", "estimativa_devolucao")
		return self.select(sql, values, fields, Carro)
	
	def listarWhereId(self, id=0,carro=Carro()):
		sql = "SELECT * FROM Carros WHERE id = ?;"
		values = (id or carro.id,)
		fields = ("id", "cor", "multa", "placa", "modelo", "taxa_dia", "estimativa_devolucao")
		carros = self.select(sql, values, fields, Carro)
		return None if len(carros) == 0 else carros[0]

	def deletar(self, id=0,carro=Carro()):
		sql = "DELETE FROM Carros WHERE id = ?;"
		values = (id or carro.id,)
		return self.delete(sql, values)