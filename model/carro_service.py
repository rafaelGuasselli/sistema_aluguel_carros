from model.carro_mapper import CarroMapper

class CarroService:
	def __init__(self):
		self.carroMapper = CarroMapper()
	
	def criar(self, carro):
		carroId = self.carroMapper.criar(carro)
		if not carroId:
			raise Exception("Falha ao adicionar carro no banco de dados!")
		return carroId

	def atualizar(self, carro):
		atualizado = self.carroMapper.atualizar(carro)
		if not atualizado:
			raise Exception("Falha ao atualizar carro no banco de dados!")

	def listar(self, id=0, carro=None):
		carros = False
		if id or carro:
			carros = self.carroMapper.listarWhereId(id=id,carro=carro)
		else:
			carros = self.carroMapper.listar()
		
		if not carros:
			raise Exception("Falha ao ler carros no banco de dados!")
		
		return carros

	def deletar(self, carro):
		deletado = self.carroMapper.deletar(carro=carro)
		if not deletado:
			raise Exception("Falha ao deletar carro no banco de dados!")
