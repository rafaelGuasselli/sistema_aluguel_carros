import tkinter as Tk

class JanelaFormularioCarro(Tk.Toplevel):
	def __init__(self, controller):
		super().__init__()
		self.controller = controller

		self.resizable(False,False)
		self.geometry("400x250")

	def inicializar(self, placa="", modelo="", taxaHora="", cor="", taxaDia=""):
		self.__removerTodosOsElementosDaJanela()
		self.container = Tk.Frame(self)
		self.container.columnconfigure(0, weight=2)
		self.container.columnconfigure(1, weight=3)
		self.container.columnconfigure(2, weight=1)
		self.container.pack(fill=Tk.BOTH, expand=True, padx=10, pady=10)

		self.__adicionarCampoPlaca(texto=placa)
		self.__adicionarCampoModelo(texto=modelo)
		self.__adicionarCampoCor(texto=cor)
		self.__adicionarCampoTaxaDiaria(texto=taxaDia)
		self.__adicionarCampoTaxaHora(texto=taxaHora)
		self.__adicionarBotaoFinalizar()

	def __adicionarCampoPlaca(self, texto=""):
		Tk.Label(self.container, text="Placa:").grid(column=0, row=0, sticky="W", pady=(0,10))
		self.inputPlaca = Tk.Entry(self.container)
		self.inputPlaca.grid(column=1, row=0, sticky="WE", pady=(0,10))

		self.inputPlaca.insert(0, texto)

	def __adicionarCampoModelo(self, texto=""):
		Tk.Label(self.container, text="Modelo:").grid(column=0, row=1, sticky="W", pady=(0,10))
		self.inputModelo = Tk.Entry(self.container)
		self.inputModelo.grid(column=1, row=1, sticky="WE", pady=(0,10))
	
		self.inputModelo.insert(0, texto)
	
	def __adicionarCampoCor(self, texto=""):
		Tk.Label(self.container, text="Cor:").grid(column=0, row=2, sticky="W", pady=(0,10))
		self.inputCor = Tk.Entry(self.container)
		self.inputCor.grid(column=1, row=2, sticky="WE", pady=(0,10))
		
		self.inputCor.insert(0, texto)

	def __adicionarCampoTaxaDiaria(self, texto=""):
		Tk.Label(self.container, text="Taxa diária:").grid(column=0, row=3, sticky="W", pady=(0,10))
		self.inputTaxaDiaria = Tk.Entry(self.container)
		self.inputTaxaDiaria.grid(column=1, row=3, sticky="WE", pady=(0,10))
		
		self.inputTaxaDiaria.insert(0, texto)

	
	def __adicionarCampoTaxaHora(self, texto=""):
		Tk.Label(self.container, text="Taxa p/ hora:").grid(column=0, row=4, sticky="W", pady=(0,10))
		self.inputTaxaHora = Tk.Entry(self.container)
		self.inputTaxaHora.grid(column=1, row=4, sticky="WE", pady=(0,10))

		self.inputTaxaHora.insert(0, texto)

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