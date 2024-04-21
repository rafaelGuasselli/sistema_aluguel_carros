import tkinter as Tk
from view.container_scrollavel import ContainerScrollavel

class ListaScrollavel(ContainerScrollavel):
	def __init__(self, parent):
		super().__init__(parent)

	def criarLista(self, controller, lista=[], alugar=False, editar=False, remover=False):
		self.controller = controller
		for elemento in lista:
			self.__adicionarElemento(
				texto = str(elemento),
				alugar=alugar,
				editar=editar,
				remover=remover,
				onAlugar=lambda: self.controller.alugar(elemento),
				onEditar=lambda: self.controller.editar(elemento),
				onRemover=lambda: self.controller.remover(elemento)
			)

	def __adicionarElemento(self, texto, onAlugar, onEditar, onRemover, alugar=False, editar=False, remover=False):
		containerCarro = Tk.Frame(self.container)
		containerCarro.columnconfigure(0, weight=3)
		containerCarro.columnconfigure(1, weight=2)
		containerCarro.pack(expand=True, fill='both', pady=(0,10), padx=10)
		containerCarro.config(background="green")

		label = Tk.Label(containerCarro, text=texto, justify="left")
		label.grid(column=0, row=0, sticky="W")

		containerButtons = Tk.Frame(containerCarro)
		containerButtons.grid(row=0, column=1, sticky="E")

		if alugar: self.__adicionarBotaoAlugar(containerButtons, onAlugar)
		if editar: self.__adicionarBotaoEditar(containerButtons, onEditar)
		if remover: self.__adicionarBotaoRemover(containerButtons, onRemover)
		

	def __adicionarBotaoRemover(self, container, onclick):
		botaoRemover = Tk.Button(container, text="Remover")
		botaoRemover.pack(side="right")
		botaoRemover.command = onclick

	def __adicionarBotaoEditar(self, container, onclick):
		botaoEditar = Tk.Button(container, text="Editar")
		botaoEditar.pack(side="right", padx=(10,0))	
		botaoEditar.command = onclick		
	
	def __adicionarBotaoAlugar(self, container, onclick):
		botaoAlugar = Tk.Button(container, text="Alugar")
		botaoAlugar.pack(side="right", padx=10)
		botaoAlugar.command = onclick