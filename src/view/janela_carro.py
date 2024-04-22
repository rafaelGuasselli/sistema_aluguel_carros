import tkinter as Tk

from controller.janela_carro_controller import JanelaCarroController 

class JanelaCarro(Tk.Toplevel):
	def __init__(self, gerenciador, carro):
		super().__init__()
		self.gerenciador = gerenciador
		self.controller = JanelaCarroController(gerenciador, self)
		self.carro = carro
		self.resizable(False,False)
		self.inicializar()

	def inicializar(self):
		self.__removerTodosOsElementosDaJanela()
		self.geometry("400x250")
		self.title("Carro")
		self.container = Tk.Frame(self)
		self.container.columnconfigure(0, weight=2)
		self.container.columnconfigure(1, weight=3)
		self.container.columnconfigure(2, weight=1)
		self.container.pack(fill=Tk.BOTH, expand=True, padx=10, pady=10)

		self.__adicionarCampoPlaca()
		self.__adicionarCampoModelo()
		self.__adicionarCampoTaxaHora()
		self.__adicionarCampoCor()
		self.__adicionarCampoTaxaDiaria()
		self.__adicionarCampoCor()
		self.__adicionarBotaoFinalizar()

	def __adicionarCampoPlaca(self):
		Tk.Label(self.container, text="Placa:").grid(column=0, row=0, sticky="W", pady=(0,10))
		self.inputPlaca = Tk.Entry(self.container)
		self.inputPlaca.insert(0, self.carro.placa)
		self.inputPlaca.grid(column=1, row=0, sticky="WE", pady=(0,10))
	
	def __adicionarCampoModelo(self):
		Tk.Label(self.container, text="Modelo:").grid(column=0, row=1, sticky="W", pady=(0,10))
		self.inputModelo = Tk.Entry(self.container)
		self.inputModelo.insert(0, self.carro.modelo)
		self.inputModelo.grid(column=1, row=1, sticky="WE", pady=(0,10))
	
	def __adicionarCampoCor(self):
		Tk.Label(self.container, text="Cor:").grid(column=0, row=2, sticky="W", pady=(0,10))
		self.inputCor = Tk.Entry(self.container)
		self.inputCor.insert(0, self.carro.cor)
		self.inputCor.grid(column=1, row=2, sticky="WE", pady=(0,10))

	def __adicionarCampoTaxaDiaria(self):
		Tk.Label(self.container, text="Taxa diária:").grid(column=0, row=3, sticky="W", pady=(0,10))
		self.inputTaxaDiaria = Tk.Entry(self.container)
		self.inputTaxaDiaria.insert(0, self.carro.taxa_dia)
		self.inputTaxaDiaria.grid(column=1, row=3, sticky="WE", pady=(0,10))
	
	def __adicionarCampoTaxaHora(self):
		Tk.Label(self.container, text="Taxa p/ hora:").grid(column=0, row=4, sticky="W", pady=(0,10))
		self.inputTaxaHora = Tk.Entry(self.container)
		self.inputTaxaHora.insert(0, self.carro.taxa_hora)
		self.inputTaxaHora.grid(column=1, row=4, sticky="WE", pady=(0,10))

	def __adicionarBotaoFinalizar(self):
		Tk.Button(self.container, command=self.controller.finalizar, text="Finalizar").grid(column=1, row=5, pady=(0,10))

	def getPlaca(self):
		return self.inputPlaca.get()

	def getModelo(self):
		return self.inputModelo.get()

	def getCor(self):
		return self.inputCor.get()
	
	def getTaxaDiaria(self):
		return self.inputTaxaDiaria.get()
	
	def getTaxaHora(self):
		return self.inputTaxaHora.get()

	def __removerTodosOsElementosDaJanela(self):
		for child in self.winfo_children(): 
			child.destroy()