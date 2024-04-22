import tkinter as Tk

from controller.janela_aluga_controller import JanelaAlugaController 

class JanelaAluga(Tk.Toplevel):
	def __init__(self, gerenciador, carro):
		super().__init__()
		self.gerenciador = gerenciador
		self.controller = JanelaAlugaController(gerenciador, self)
		self.carro = carro
		self.inicializar()
		

	def inicializar(self):
		self.__removerTodosOsElementosDaJanela()
		self.geometry("400x180")
		self.container = Tk.Frame(self)
		self.container.columnconfigure(0, weight=2)
		self.container.columnconfigure(1, weight=3)
		self.container.columnconfigure(2, weight=1)
		self.container.pack(fill=Tk.BOTH, expand=True, padx=10, pady=10)

		self.__adicionarCampoCPF()
		self.__adicionarCampoNome()
		self.__adicionarBotaoFinalizar()


	def __adicionarCampoCPF(self):
		Tk.Label(self.container, text="CPF:").grid(column=0, row=0, sticky="W", pady=(0,10))
		self.inputCPF = Tk.Entry(self.container)
		self.inputCPF.grid(column=1, row=0, sticky="WE", pady=(0,10))
		Tk.Button(self.container,command=self.controller.procurar, text="Procurar").grid(column=3, row=0, sticky="E", pady=(0,10))
	
	def __adicionarCampoNome(self):
		Tk.Label(self.container, text="Nome:").grid(column=0, row=1, sticky="W", pady=(0,10))
		self.inputNome = Tk.Entry(self.container)
		self.inputNome.grid(column=1, row=1, sticky="WE", pady=(0,10))

	def __adicionarBotaoFinalizar(self):
		Tk.Button(self.container, command=self.controller.cadastrar, text="Finalizar").grid(column=1, row=3, pady=(0,10))

	def getNome(self):
		return self.inputNome.get()

	def getCPF(self):
		print("AAA")
		return self.inputCPF.get()

	def setNome(self, nome):
		self.inputNome.delete(0,Tk.END)
		self.inputNome.insert(0,nome)

	def __removerTodosOsElementosDaJanela(self):
		for child in self.winfo_children(): 
			child.destroy()

		
