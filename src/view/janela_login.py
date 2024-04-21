import tkinter as Tk
from controller.janela_login_controller import JanelaLoginController

class JanelaLogin(Tk.Toplevel):
	def __init__(self, gerenciador):
		super().__init__()
		self.gerenciador = gerenciador
		self.controller = JanelaLoginController(gerenciador, self)
		self.inicializar()
	
	def inicializar(self):
		self.__removerTodosOsElementosDaJanela()

		self.geometry("400x300")
		self.container = Tk.Frame(self)
		self.container.columnconfigure(0, weight=1)
		self.container.columnconfigure(1, weight=8, minsize=250)
		self.container.place(in_=self, anchor='center', relx=.5, rely=.5)

		self.__adicionarInputDoCpf(self.container)
		self.__adicionarInputDeSenha(self.container)
		self.__adicionarBotaoDeLogin(self.container, self.controller.login)

	def getCPF(self):
		return self.inputCPF.get()

	def getSenha(self):
		return self.inputSenha.get()

	def __adicionarInputDoCpf(self, container):
		self.labelCPF = Tk.Label(container, text="CPF: ", font=("Arial", 16, "bold"), justify="left").grid(sticky="W",column=0, row=0)
		self.inputCPF = Tk.Entry(container, name="cpf")
		self.inputCPF.grid(column=1, row=0, sticky="ew")
	
	def __adicionarInputDeSenha(self, container):
		self.labelSenha = Tk.Label(container, text="Senha: ", font=("Arial", 16, "bold"), justify="left").grid(sticky="W",column=0, row=1)
		self.inputSenha = Tk.Entry(container, name="password", show="*")
		self.inputSenha.grid(column=1, row=1, sticky="ew")

	def __adicionarBotaoDeLogin(self, container, onclick):
		self.botaoLogin = Tk.Button(container, text="Login", font=("Arial", 14), command=onclick).grid(row=2, columnspan=2, pady=(10,0))

	def __removerTodosOsElementosDaJanela(self):
		for child in self.winfo_children(): 
			child.destroy()