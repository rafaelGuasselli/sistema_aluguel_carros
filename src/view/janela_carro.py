import tkinter as Tk
from tkinter import ttk
from tkinter.constants import *
from view.lista_scrollavel import ListaScrollavel
from controller.janela_carro_controller import JanelaCarroController

class JanelaCarros(Tk.Tk):
	def __init__(self, gerenciador, listaCarros=[], gerenciarUsuarios=False, adicionarCarros=False, editarCarros=False, alugarCarros=False, removerCarros=False, pagarCarros=False):
		super().__init__()
		self.geometry("1200x600")
		self.gerenciador = gerenciador
		self.controller = JanelaCarroController(gerenciador, self)
		self.inicializar(listaCarros, gerenciarUsuarios, adicionarCarros, editarCarros, alugarCarros, removerCarros, pagarCarros)

	def inicializar(self, listaCarros=[], gerenciarUsuarios=False, adicionarCarros=False, editarCarros=False, alugarCarros=False, removerCarros=False, pagarCarros=False):
		self.__removerTodosOsElementosDaJanela()
		self.title("Janela Carro")
		self.rowconfigure(2, weight=10)
		self.columnconfigure(0, weight=1)

		self.__adicionarSuperior(gerenciarUsuarios=gerenciarUsuarios, adicionarCarros=adicionarCarros)
		self.__criaSeparadorSuperiorCentral()
		self.__adicionarListaDeCarros(
			listaCarros=listaCarros,
			editar=editarCarros, 
			alugar=alugarCarros, 
			remover=removerCarros,
			pagar=pagarCarros
		)


	def __criaSeparadorSuperiorCentral(self):
		ttk.Separator(self, orient="horizontal").grid(sticky="WE", column=0, row=1)

	def __adicionarListaDeCarros(self, listaCarros=[], editar=False, alugar=False, remover=False, pagar=False):
		self.lista = ListaScrollavel(self)
		self.lista.criarLista(self.controller, listaCarros, alugar, editar, remover, pagar)
		self.lista.grid(sticky="WE", row=2, column=0)

	def __adicionarBotaoLogin(self, container):
		self.botaoLogin = Tk.Button(container, text="Login", command=self.controller.telaLogin)
		self.botaoLogin.pack(side="right", padx=(0,20), pady=10)

	def __adicionarBotaoLogout(self, container):
		self.botaoLogout = Tk.Button(container, text="Logout", command=self.controller.logout)
		self.botaoLogout.pack(side="right", padx=(0,20), pady=10)

	def __adicionarSuperior(self, gerenciarUsuarios=False, adicionarCarros=False):
		self.superior = Tk.Frame(self)
		self.superior.grid(row=0, sticky="NSWE")

		self.__adicionarLabelVeiculos(self.superior)
		self.__adicionarBotaoLogout(self.superior)
		self.__adicionarBotaoLogin(self.superior)

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