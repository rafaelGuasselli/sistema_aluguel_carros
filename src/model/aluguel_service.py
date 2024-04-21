from .carro_service import CarroService
from .cliente_service import ClienteService

class AluguelService:
	def __init__(self):
		self.carroService = CarroService()
		self.clienteService = ClienteService()
	
	def alugar(self, carro, cliente):
		try:
			return self.__alugar(carro, cliente)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao alugar carro!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __alugar(self, carro, cliente):
		carro = self.carroService.listar(carro=carro)
		clienteNoBanco = self.clienteService.listar(cliente=cliente)
		
		if carro is None:
			raise Exception("Carro não existe!")
		
		if clienteNoBanco is None:
			self.clienteService.criar(cliente=cliente)
		else:
			self.clienteService.atualizar(cliente=cliente)

		if carro.cliente_id != None:
			raise Exception("Carro já está alugado!")

		carro.cliente_id = cliente.id
		self.carroService.atualizar(carro=carro)
	
	def pagar(self, carro):
		try:
			return self.__pagar(carro)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao pagar carro!\n{}".format(detalhes)
			raise Exception(mensagem)

	def __pagar(self, carro):
		carro = self.carroService.listar(carro=carro)

		if carro is None:
			raise Exception("Carro não existe!")
		
		carro.cliente_id = None
		carro.estimativa_devolucao = None
		self.carroService.atualizar(carro)

