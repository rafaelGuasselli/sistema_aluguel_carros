from model.carro_mapper import CarroMapper
from model.cliente_mapper import ClienteMapper

class AluguelService:
	def __init__(self):
		self.carroMapper = CarroMapper()
		self.clienteMapper = ClienteMapper()
	
	def alugar(self, carro, cliente):
		carro = self.carroMapper.listarWhereId(carro=carro)
		clienteNoBanco = self.clienteMapper.listarWhereCpf(cliente=cliente)
		
		if carro is None:
			raise Exception("Carro não existe!")
		
		if clienteNoBanco is None:
			self.clienteMapper.criar(cliente=cliente)
		else:
			self.clienteMapper.atualizar(cliente=cliente)

		if carro.cliente_id != None:
			raise Exception("Carro já está alugado!")

		carro.cliente_id = cliente.id
		self.carroMapper.atualizar(carro=carro)
	
	def pagar(self, carro):
		carro = self.carroMapper.listarWhereId(carro=carro)

		if carro is None:
			raise Exception("Carro não existe!")
		
		carro.cliente_id = None
		carro.estimativa_devolucao = None
		self.carroMapper.atualizar(carro)

