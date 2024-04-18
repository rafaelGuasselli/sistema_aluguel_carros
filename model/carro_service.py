from model.carro_mapper import CarroMapper

class CarroService:
	def __init__(self):
		self.carroMapper = CarroMapper()
	
	def criar(self, carro):
		try:
			return self.carroMapper.criar(carro)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao adicionar carro no banco de dados!\n{detalhes}"
			raise Exception(mensagem)

	def atualizar(self, carro):
		try:
			carroId = self.carroMapper.atualizar(carro)
			return carroId
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao atualizar carro no banco de dados!\n{detalhes}"
			raise Exception(mensagem)

	def listar(self, id=0, carro=None):
		try:
			return self.__listar(id, carro)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao ler carros no banco de dados!\n{detalhes}"
			raise Exception(mensagem)

	def __listar(self, id=0, carro=None):
		carros = False
		if id or carro:
			carros = self.carroMapper.listarId(id=id,carro=carro)
		else:
			carros = self.carroMapper.listar()		
		return carros

	def deletar(self, carro):
		try:
			self.carroMapper.deletar(carro=carro)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao deletar carro no banco de dados!\n{detalhes}"
			raise Exception(mensagem)