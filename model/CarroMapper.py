import sqlite3
from .Carro import Carro

class CarroMapper:
	def __init__(self):
		self.connection = sqlite3.connect("aluguel_carros.db")
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()

	
	def __del__(self):
		self.connection.close()

	def insert(self, carro):
		try:
			self.cursor.execute("INSERT INTO Carros(id, cor, multa, placa, modelo, taxa_dia, estimativa_devolucao) VALUES (1, ?,?,?,?,?,?);", (carro.cor, carro.multa, carro.placa, carro.modelo, carro.taxa_dia, carro.estimativa_devolucao))
			self.connection.commit()
			return True
		except sqlite3.Error as error:
			print(error.sqlite_errorcode)
			print(error.sqlite_errorname)
			print(error.sqlite3_errmsg)
			return False 
	
	def update(self, carro):
		try:
			self.cursor.execute("UPDATE Carros SET cor = ?, multa = ?, placa = ?, modelo = ?, taxa_dia = ?, estimativa_devolucao = ? WHERE id = ?;", (carro.cor, carro.multa, carro.placa, carro.modelo, carro.taxa_dia, carro.estimativa_devolucao, carro.id))
			self.connection.commit()
			return True
		except sqlite3.Error as error:
			print(error.sqlite_errorcode)
			print(error.sqlite_errorname)
			print(error.sqlite3_errmsg)
			return False 
	
	def select(self):
		try:
			self.cursor.execute("SELECT * FROM Carros;")
			carros = []
			for row in self.cursor:
				carro = Carro(row["id"])
				carro.cor = row["cor"]
				carro.multa = row["multa"]
				carro.placa = row["placa"]
				carro.modelo = row["modelo"]
				carro.taxa_dia = row["taxa_dia"]
				carro.estimativa_devolucao = row["estimativa_devolucao"]
				carros.append(carro)

			return carros
		except sqlite3.Error as error:
			print(error.sqlite_errorcode)
			print(error.sqlite_errorname)
			print(error.sqlite3_errmsg)
			return [] 
	
	def delete(self, carro):
		try:
			self.cursor.execute("DELETE FROM Carros WHERE id = ?;", (carro.id, ))
			self.connection.commit()
			return True
		except sqlite3.Error as error:
			print(error)
			return False 