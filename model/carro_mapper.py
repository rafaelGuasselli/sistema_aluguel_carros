import sqlite3
from .carro import Carro

class CarroMapper:
	def __init__(self):
		self.connection = sqlite3.connect("aluguel_carros.db")
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()

	
	def __del__(self):
		self.connection.close()

	def insert(self, carro):
		sql = "INSERT INTO Carros(cor, multa, placa, modelo, taxa_dia, estimativa_devolucao) VALUES (?,?,?,?,?,?);"
		values = (carro.cor, carro.multa, carro.placa, carro.modelo, carro.taxa_dia, carro.estimativa_devolucao)
		return self.__insert(sql, values)	
	
	def update(self, carro):
		sql = "UPDATE Carros SET cor = ?, multa = ?, placa = ?, modelo = ?, taxa_dia = ?, estimativa_devolucao = ? WHERE id = ?;"
		values = (carro.cor, carro.multa, carro.placa, carro.modelo, carro.taxa_dia, carro.estimativa_devolucao, carro.id)
		return self.__update(sql, values)
		
	def select(self):
		sql = "SELECT * FROM Carros;"
		values = ()
		return self.__select(sql, values)
	
	def selectWhereId(self, id=0,carro=Carro()):
		sql = "SELECT * FROM Carros WHERE id = ?;"
		values = (id or carro.id,)
		carros = self.__select(sql, values)
		return None if len(carros) == 0 else carros[0]

	def delete(self, id=0,carro=Carro()):
		sql = "DELETE FROM Carros WHERE id = ?;"
		values = (id or carro.id,)
		return self.__delete(sql, values)

	
	def __insert(self, sql, values):
		try:
			self.cursor.execute(sql, values)
			self.connection.commit()
			
			return self.cursor.lastrowid
		except sqlite3.Error as error:
			print(error)
			return False 
	

	def __update(self, sql, values):
		try:
			self.cursor.execute(sql, values)
			self.connection.commit()
			return True
		except sqlite3.Error as error:
			print(error)
			return False 

	def __select(self, sql, values):
		try:
			self.cursor.execute(sql, values)
			carros = []
			for row in self.cursor:
				carro = Carro()
				carro.id = row["id"]
				carro.cor = row["cor"]
				carro.multa = row["multa"]
				carro.placa = row["placa"]
				carro.modelo = row["modelo"]
				carro.taxa_dia = row["taxa_dia"]
				carro.estimativa_devolucao = row["estimativa_devolucao"]
				carros.append(carro)

			return carros
		except sqlite3.Error as error:
			print(error)
			return [] 

	def __delete(self, sql, values):
		try:
			self.cursor.execute(sql, values)
			self.connection.commit()
			return True
		except sqlite3.Error as error:
			print(error)
			return False 