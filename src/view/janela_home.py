import tkinter as Tk
from tkinter import ttk
from tkinter.constants import *
from view.lista_scrollavel import ListaScrollavel
from controller.janela_home_controller import JanelaHomeController

class JanelaHome(Tk.Tk):
	def __init__(self, gerenciador):
		super().__init__()
		self.geometry("1200x600")
		self.gerenciador = gerenciador
		self.controller = JanelaHomeController(gerenciador, self)
		self.inicializar()

	def inicializar(self, listaCarros=[], gerenciarUsuarios=False, adicionarCarros=False, editarCarros=False, alugarCarros=False, removerCarros=False, pagarCarros=False):
		self.__removerTodosOsElementosDaJanela()
		self.title("Home")
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
		self.botaoGerenciarUsuarios = Tk.Button(container, text="Gerenciar usuários", command=self.controller.telaUsuarios)
		self.botaoGerenciarUsuarios.pack(side="right", padx=(0,20), pady=10)

	def __adicionarBotaoAdicionarCarros(self, container):
		self.botaoAdicionarCarros = Tk.Button(container, text="Adicionar carros", command=self.controller.telaCriarCarros)
		self.botaoAdicionarCarros.pack(side="right", padx=(0,20), pady=10)
		
	def __adicionarLabelVeiculos(self, container):
		self.labelVeiculos = Tk.Label(container, text="Veículos", font=("Arial", 18, "bold"))
		self.labelVeiculos.pack(side="left", padx=(10,0))

	def __removerTodosOsElementosDaJanela(self):
		for child in self.winfo_children(): 
			child.destroy()