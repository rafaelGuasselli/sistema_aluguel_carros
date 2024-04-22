import tkinter as Tk
from view.container_scrollavel import ContainerScrollavel
from functools import partial

class ListaCarroScrollavel(ContainerScrollavel):
	def __init__(self, parent, *args, **kw):
		super().__init__(parent, *args, **kw)

	def criarLista(self, controller, lista=[], alugar=False, editar=False, remover=False, pagar=False):
		self.controller = controller
		for linha, elemento in enumerate(lista):
			funcAlugar = partial(self.controller.alugar, elemento)
			funcEditar = partial(self.controller.editar, elemento)
			funcPagar = partial(self.controller.pagar, elemento)
			funcRemover = partial(self.controller.remover, elemento)
			self.__adicionarElemento(
				linha,
				carro=elemento,
				alugar=alugar,
				editar=editar,
				pagar=pagar,
				remover=remover,
				onAlugar=funcAlugar,
				onPagar=funcPagar,
				onEditar=funcEditar,
				onRemover=funcRemover
			)

	def __adicionarElemento(self, linha, carro, onAlugar, onPagar, onEditar, onRemover, alugar=False, pagar=False, editar=False, remover=False):
		# containerCarro = Tk.Frame(self.container)
		self.container.columnconfigure((0,1,2,3,4,5,6), weight=1)
		self.container.columnconfigure(7, weight=3)

		Tk.Label(self.container, text="Modelo: " + carro.modelo).grid(row=linha, column=0, sticky="W", padx=(10,0) )
		Tk.Label(self.container, text="Placa: " + carro.placa).grid(row=linha, column=1, sticky="W")
		Tk.Label(self.container, text="Cor: " + carro.cor).grid(row=linha, column=2, sticky="W")
		Tk.Label(self.container, text="Taxa hora: " + str(carro.taxa_hora)).grid(row=linha, column=3, sticky="W")
		Tk.Label(self.container, text="Taxa diária: " + str(carro.taxa_dia)).grid(row=linha, column=4, sticky="W")
		Tk.Label(self.container, text="Data alguel: " + str(carro.data_aluguel)).grid(row=linha, column=5, sticky="W")
		Tk.Label(self.container, text="Alugado: " + str(carro.estaAlugado())).grid(row=linha, column=6, sticky="W")

		containerButtons = Tk.Frame(self.container)
		containerButtons.grid(row=linha, column=7, sticky="E")

		if alugar: self.__adicionarBotaoAlugar(containerButtons, onAlugar)
		if pagar: self.__adicionarBotaoPagar(containerButtons,onPagar)
		if editar: self.__adicionarBotaoEditar(containerButtons, onEditar)
		if remover: self.__adicionarBotaoRemover(containerButtons, onRemover)
		
	def __adicionarBotaoPagar(self, container, onclick):
		botaoPagar = Tk.Button(container, text="Pagar", command=onclick)
		botaoPagar.pack(side="right")

	def __adicionarBotaoRemover(self, container, onclick):
		botaoRemover = Tk.Button(container, text="Remover", command=onclick)
		botaoRemover.pack(side="right")

	def __adicionarBotaoEditar(self, container, onclick):
		botaoEditar = Tk.Button(container, text="Editar", command=onclick)
		botaoEditar.pack(side="right", padx=(10,10))	
				
	def __adicionarBotaoAlugar(self, container, onclick):
		botaoAlugar = Tk.Button(container, text="Alugar", command=onclick)
		botaoAlugar.pack(side="right", padx=10)
