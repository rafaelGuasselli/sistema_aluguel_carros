import tkinter as Tk

class JanelaAluga(Tk.Toplevel):
	def __init__(self, master) -> None:
		super().__init__(master)
		self.geometry("400x180")
		self.container = Tk.Frame(self)
		self.container.columnconfigure(0, weight=2)
		self.container.columnconfigure(1, weight=3)
		self.container.columnconfigure(2, weight=1)
		# self.container.rowconfigure((0,1,2,3), weight=1)
		self.__create_gidgets()
		self.container.pack(fill=Tk.BOTH, expand=True, padx=10, pady=10)

	def __create_gidgets(self):
		Tk.Label(self.container, text="CPF:").grid(column=0, row=0, sticky="W", pady=(0,10))
		Tk.Label(self.container, text="Nome:").grid(column=0, row=1, sticky="W", pady=(0,10))
		Tk.Label(self.container, text="Senha:").grid(column=0, row=2, sticky="W", pady=(0,10))
		Tk.Button(self.container,command=self.__click_procurar_event, text="Procurar").grid(column=3, row=0, sticky="E", pady=(0,10))
		Tk.Entry(self.container).grid(column=1, row=0, sticky="WE", pady=(0,10))
		Tk.Entry(self.container).grid(column=1, row=1, sticky="WE", pady=(0,10))
		Tk.Entry(self.container).grid(column=1, row=2, sticky="WE", pady=(0,10))
		Tk.Button(self.container, command=self.__click_finalizar_event, text="Finalizar").grid(column=1, row=3, pady=(0,10))
		
