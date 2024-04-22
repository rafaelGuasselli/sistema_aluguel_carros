import tkinter as Tk
from view.container_scrollavel import ContainerScrollavel
from functools import partial

class ListaScrollavel(ContainerScrollavel):
	def __init__(self, parent, *args, **kw):
		super().__init__(parent, *args, **kw)

	def criarLista(self, controller, lista=[], alugar=False, editar=False, remover=False):
		self.controller = controller
		for elemento in lista:
			funcAlugar = partial(self.controller.alugar, elemento)
			funcEditar = partial(self.controller.editar, elemento)
			funcRemover = partial(self.controller.remover, elemento)
			self.__adicionarElemento(
				texto = str(elemento),
				alugar=alugar,
				editar=editar,
				remover=remover,
				onAlugar=funcAlugar,
				onEditar=funcEditar,
				onRemover=funcRemover
			)

	def __adicionarElemento(self, texto, onAlugar, onEditar, onRemover, alugar=False, editar=False, remover=False):
		containerCarro = Tk.Frame(self.container)
		containerCarro.columnconfigure(0, weight=3)
		containerCarro.columnconfigure(1, weight=2)
		
		containerCarro.pack(expand=True, fill='both', pady=(0,10), padx=10)

		label = Tk.Label(containerCarro, text=texto, justify="left")
		label.grid(column=0, row=0, sticky="W")

		containerButtons = Tk.Frame(containerCarro)
		containerButtons.grid(row=0, column=1, sticky="E")

		if alugar: self.__adicionarBotaoAlugar(containerButtons, onAlugar)
		if editar: self.__adicionarBotaoEditar(containerButtons, onEditar)
		if remover: self.__adicionarBotaoRemover(containerButtons, onRemover)
		

	def __adicionarBotaoRemover(self, container, onclick):
		botaoRemover = Tk.Button(container, text="Remover", command=onclick)
		botaoRemover.pack(side="right")

	def __adicionarBotaoEditar(self, container, onclick):
		botaoEditar = Tk.Button(container, text="Editar", command=onclick)
		botaoEditar.pack(side="right", padx=(10,0))	
				
	def __adicionarBotaoAlugar(self, container, onclick):
		botaoAlugar = Tk.Button(container, text="Alugar", command=onclick)
		botaoAlugar.pack(side="right", padx=10)
