import tkinter as Tk
from tkinter.constants import *
from view.lista_scrollavel import ListaScrollavel
from controller.janela_carro_controller import JanelaCarroController

class JanelaCarros(Tk.Tk):
	def __init__(self, gerenciador, listaCarros=[], gerenciarUsuarios=False, adicionarCarros=False, editarCarros=False, alugarCarros=False, removerCarros=False):
		super().__init__()
		self.gerenciador = gerenciador
		self.controller = JanelaCarroController(gerenciador, self)
		self.inicializar(listaCarros, gerenciarUsuarios, adicionarCarros, editarCarros, alugarCarros, removerCarros)
		self.mainloop()

	def inicializar(self, listaCarros=[], gerenciarUsuarios=False, adicionarCarros=False, editarCarros=False, alugarCarros=False, removerCarros=False):
		self.__removerTodosOsElementosDaJanela()
		self.geometry("800x600")
		self.rowconfigure(1, weight=10)
		self.columnconfigure(0, weight=1)
		self.columns = [0,2,4] # Alugar, editar carros, editar usuários 

		self.__adicionarSuperior(gerenciarUsuarios=gerenciarUsuarios, adicionarCarros=adicionarCarros)
		self.__adicionarListaDeCarros(
			listaCarros=listaCarros,
			editar=editarCarros, 
			alugar=alugarCarros, 
			remover=removerCarros
		)

	def __adicionarListaDeCarros(self, listaCarros=[], editar=False, alugar=False, remover=False):
		self.lista = ListaScrollavel(self)
		self.lista.criarLista(self.controller, listaCarros, alugar, editar, remover)
		self.lista.grid(sticky="WE", row=1, column=0)

	def __adicionarSuperior(self, gerenciarUsuarios=False, adicionarCarros=False):
		self.superior = Tk.Frame(self)
		self.superior.grid(row=0, sticky="NSWE")

		self.__adicionarLabelVeiculos(self.superior)
		if adicionarCarros: self.__adicionarBotaoAdicionarCarros(self.superior)
		if gerenciarUsuarios: self.__adicionarBotaoGerenciarUsuario(self.superior)

	def __adicionarBotaoGerenciarUsuario(self, container):
		self.botaoGerenciarUsuarios = Tk.Button(container, text="Gerenciar usuários")
		self.botaoGerenciarUsuarios.pack(side="right", padx=(0,20), pady=10)

	def __adicionarBotaoAdicionarCarros(self, container):
		self.botaoAdicionarCarros = Tk.Button(container, text="Adicionar carros")
		self.botaoAdicionarCarros.pack(side="right", padx=(0,20), pady=10)
		
	def __adicionarLabelVeiculos(self, container):
		self.labelVeiculos = Tk.Label(container, text="Veículos", font=("Arial", 18, "bold"))
		self.labelVeiculos.pack(side="left", padx=(10,0))

	def __removerTodosOsElementosDaJanela(self):
		for child in self.winfo_children(): 
			child.destroy()