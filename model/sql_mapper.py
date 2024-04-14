import sqlite3
class SqlMapper:
	def __init__(self):
		self.connection = sqlite3.connect("aluguel_carros.db")
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()

	def __del__(self):
		self.connection.close()
	
	def _insert(self, sql, values):
		try:
			self.cursor.execute(sql, values)
			self.connection.commit()
			
			return self.cursor.lastrowid
		except sqlite3.Error as error:
			print(error)
			return False 
	

	def _update(self, sql, values):
		try:
			self.cursor.execute(sql, values)
			self.connection.commit()
			return True
		except sqlite3.Error as error:
			print(error)
			return False 

	def _select(self, sql, values, fields, instanciar):
		try:
			self.cursor.execute(sql, values)
			lista = []
			for row in self.cursor:
				instancia = instanciar()
				for field in fields:
					setattr(instancia, field, row[field])
				lista.append(instancia)

			return lista
		except sqlite3.Error as error:
			print(error)
			return [] 

	def _delete(self, sql, values):
		try:
			self.cursor.execute(sql, values)
			self.connection.commit()
			return True
		except sqlite3.Error as error:
			print(error)
			return False 