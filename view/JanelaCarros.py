import tkinter as Tk
from view.Lista import Lista
from view.JanelaCriarCarro import JanelaCriarCarro
from view.VerticalScrolledFrame import VerticalScrolledFrame

class JanelaCarros(Tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        # Alugar, editar carros, editar usuários 
        self.permissions = "111"
        self.__create_gidgets()
        self.mainloop()

    def __create_gidgets(self):
        
        superior = Tk.Frame(self, highlightbackground="blue", highlightthickness=1)
        if (self.permissions[2] == '1'):
            Tk.Button(superior, text="Gerenciar usuários", command=self.__click_gerenciar_usuarios_event).pack(side="right", padx=(0,20), pady=10)
        
        if (self.permissions[1] == '1'):
            Tk.Button(superior, text="Adicionar carros", command=self.__click_adicionar_carros_event).pack(side="right", padx=(0,20), pady=10)
        
        Tk.Label(superior, text="Veículos", font=("Arial", 18, "bold")).pack(side="left", padx=(10,0))
        
        central = Tk.Frame(self)

        verticalScrolledFrame = VerticalScrolledFrame(central)
        verticalScrolledFrame.pack(expand=True, fill=Tk.BOTH)
        Lista(verticalScrolledFrame.interior)

        central.grid(sticky="WE",row=1, column=0)
        superior.grid(row=0, column=0, sticky="NSWE")
    

    def __click_adicionar_carros_event(self):
        JanelaCriarCarro(self)
    
    def __click_gerenciar_usuarios_event(self):
        print("clicado")


