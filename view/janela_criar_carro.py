import tkinter as Tk

class JanelaCriarCarro(Tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.geometry("300x300")

        self.columnconfigure(0, minsize=50, weight=1)
        self.columnconfigure(1, weight=3)

        self.__create_gidgets()
        self.mainloop()

    def __create_gidgets(self):
        # Placa
        Tk.Label(self, text="Placa:").grid(column=0, sticky="W", padx=(10,0), pady=(10,20), row=0)
        Tk.Entry(self).grid(column=1, sticky="WE", row=0, padx=(0,10), pady=(10,20))

        # Cor
        Tk.Label(self, text="Cor:").grid(column=0, sticky="W", padx=(10,0), pady=(0,20), row=1)
        Tk.Entry(self).grid(column=1, sticky="WE", row=1, padx=(0,10), pady=(0,20))

        # Taxa diaria
        Tk.Label(self, text="Taxa diaria:").grid(column=0, sticky="W", padx=(10,0), pady=(0,20), row=2)
        Tk.Entry(self).grid(column=1, sticky="WE", row=2, padx=(0,10), pady=(0,20))

        # Taxa hora
        Tk.Label(self, text="Taxa hora:").grid(column=0, sticky="W", padx=(10,0), pady=(0,20), row=3)
        Tk.Entry(self).grid(column=1, sticky="WE", row=3, padx=(0,10), pady=(0,20))

        # Multa
        Tk.Label(self, text="Multa:").grid(column=0, sticky="W", padx=(10,0), pady=(0,20), row=4)
        Tk.Entry(self).grid(column=1, sticky="WE", row=4, padx=(0,10), pady=(0,20))

        # Botao adicionar
        Tk.Button(self, text="Adicionar carro", command=self.__click_adicionar_carro_button).grid(column=0, columnspan=2, sticky="S")

    def __click_adicionar_carro_button(self):
        print("criando carro")