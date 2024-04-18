from model.carro_service import CarroService
from model.cliente_service import ClienteService

class AluguelService:
	def __init__(self):
		self.carroService = CarroService()
		self.clienteService = ClienteService()
	
	def alugar(self, carro, cliente):
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
		carro = self.carroService.listar(carro=carro)

		if carro is None:
			raise Exception("Carro não existe!")
		
		carro.cliente_id = None
		carro.estimativa_devolucao = None
		self.carroService.atualizar(carro)

