from model.cliente_mapper import ClienteMapper

class ClienteService:
	def __init__(self):
		self.clienteMapper = ClienteMapper()
	
	def criar(self, cliente):
		try:
			return self.clienteMapper.criar(cliente)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao adicionar cliente no banco de dados!\n{detalhes}"
			raise Exception(mensagem)

	def atualizar(self, cliente):
		try:
			return self.clienteMapper.atualizar(cliente)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao atualizar cliente no banco de dados!\n{detalhes}"
			raise Exception(mensagem)

	def listar(self, id=0, cliente=None):
		try:
			return self.__listar(id, cliente)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao ler cliente no banco de dados!\n{detalhes}"
			raise Exception(mensagem)

	def __listar(self, id=0, cliente=None):
		clientes = False
		if id or cliente:
			clientes = self.clienteMapper.listarId(id=id,cliente=cliente)
		else:
			clientes = self.clienteMapper.listar()
		
		return clientes

	def deletar(self, cliente):
		try:
			self.clienteMapper.deletar(cliente=cliente)
		except Exception as error:
			detalhes = str(error)
			mensagem = "Falha ao deletar cliente no banco de dados!\n{detalhes}"
			raise Exception(mensagem)
