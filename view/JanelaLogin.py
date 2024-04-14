import tkinter as Tk

class JanelaLogin(Tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")

        # Configuracao de grid
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=8)
        self.columnconfigure(2, weight=1)
    
        self.__create_gidgets()

        self.mainloop()
        
    
    def __create_gidgets(self):
        # Criacao de grid para possicionar os elementos de label e entry
        dataFrame = Tk.Frame(self)
        dataFrame.columnconfigure(0, weight=1)
        dataFrame.columnconfigure(1, weight=8, minsize=250)

        # Email
        Tk.Label(dataFrame, text="Email: ", font=("Arial", 16, "bold"), justify="left").grid(sticky="W",column=0, row=0)
        emailEntry = Tk.Entry(dataFrame, name="email")
        self.email = {"get": emailEntry.get, "erase": emailEntry.delete}
        emailEntry.grid(column=1, row=0, sticky="ew")
        
        # Password
        Tk.Label(dataFrame, text="Senha: ", font=("Arial", 16, "bold"), justify="left").grid(sticky="W",column=0, row=1)
        passwordEntry = Tk.Entry(dataFrame, name="password", show="*")
        self.password = {"get": passwordEntry.get}
        passwordEntry.grid(column=1, row=1, sticky="ew")

        # Botao de login
        Tk.Button(dataFrame, text="Login", font=("Arial", 14), command=self.__click_button_event).grid(row=2, columnspan=2, pady=(10,0))

        dataFrame.grid(column=1, row=1)

    # Evento para que quando o botao de login seja clicado
    def __click_button_event(self):
        print({"email": self.email["get"](), "password": self.password["get"]()})
        self.email["erase"](0, 'end')





