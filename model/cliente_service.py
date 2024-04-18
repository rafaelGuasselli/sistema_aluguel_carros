from model.cliente_mapper import ClienteMapper

class ClienteService:
	def __init__(self):
		self.clienteMapper = ClienteMapper()
	
	def criar(self, cliente):
		clienteId = self.clienteMapper.criar(cliente)
		if not clienteId:
			raise Exception("Falha ao adicionar cliente no banco de dados!")
		return clienteId

	def atualizar(self, cliente):
		atualizado = self.clienteMapper.atualizar(cliente)
		if not atualizado:
			raise Exception("Falha ao atualizar cliente no banco de dados!")

	def listar(self, id=0, cliente=None):
		clientes = False
		if id or cliente:
			clientes = self.clienteMapper.listarWhereId(id=id,cliente=cliente)
		else:
			clientes = self.clienteMapper.listar()
		
		if clientes is False:
			raise Exception("Falha ao ler clientes no banco de dados!")
		
		return clientes

	def deletar(self, cliente):
		deletado = self.clienteMapper.deletar(cliente=cliente)
		if not deletado:
			raise Exception("Falha ao deletar cliente no banco de dados!")
