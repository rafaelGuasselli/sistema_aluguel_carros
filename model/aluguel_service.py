from model.carro import Carro
from model.cliente import Cliente
from model.carro_mapper import CarroMapper
from model.cliente_mapper import ClienteMapper

class AluguelService:
	def __init__(self):
		self.carroMapper = CarroMapper()
		self.clienteMapper = ClienteMapper()
	
	def alugar(carro, cliente):
		carro = self.carroMapper.listarWhereId(carro=carro)
		cliente = self.clienteMapper.listarWhereCpf(cliente=cliente)
		
		if carro is None:
			raise Exception("Carro não existe!")
		
		if cliente is None:
			self.clienteMapper.criar(cliente=cliente)
		else:
			self.clienteMapper.atualizar(cliente=cliente)

		if carro.cliente_id != None:
			raise Exception("Carro já está alugado!")

		carro.cliente_id = cliente.id
		self.carroMapper.atualize(carro=carro)
	
	def pagar(carro):
		carro = self.carroMapper.listarWhereId(carro=carro)

		if carro is None:
			raise Exception("Carro não existe!")
		
		carro.cliente_id = None
		self.clienteMapper.atualizar(cliente=cliente)

