import tkinter as Tk
from view.lista import Lista
from view.janela_criar_carro import JanelaCriarCarro
from view.janela_usuario import JanelaUsuarios

class JanelaCarros(Tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        # Alugar, editar carros, editar usuários 
        self.permissions = "111"
        self.columns = [0,2,4]
        self.__create_gidgets()
        self.bind("<MouseWheel>", self._on_mousewheel)
        self.bind("<Button-4>", self._on_mousewheel)
        self.bind("<Button-5>", self._on_mousewheel)

        self.mainloop()

    def _on_mousewheel(self, event):
        print(event)

    def __create_gidgets(self):
        central = Tk.Frame(self)
        central.grid(sticky="WE",row=1, column=0)
        central.bind("<MouseWheel>", self._on_mousewheel)
    
    # A partir de informacoes varios elementos carros
    def __create_cars(self, containerList):
        for i in range(21):
            containerCarro = Tk.Frame(containerList)
            containerCarro.columnconfigure(0, weight=3)
            containerCarro.columnconfigure(1, weight=2)

            Tk.Label(containerCarro, text="Modelo " + str(i), justify="left").grid(column=0, row=0, sticky="W")

            containerButtons = Tk.Frame(containerCarro)

            botaoAlugar = Tk.Button(containerButtons, text="Alugar")
            botaoRemover = Tk.Button(containerButtons, text="Remover")
            botaoEditar = Tk.Button(containerButtons, text="Editar")

            cont = self.permissions[0:2].count('1')
            if (cont == 2 and self.permissions[1] == '1'):
                cont+=1

            if (self.permissions[0] == '1'):
                botaoAlugar.pack(side="right", padx=10)


            if (self.permissions[1] == '1'):
                botaoEditar.pack(side="right", padx=(10,0))
                botaoRemover.pack(side="right")

            containerButtons.grid(row=0, column=1, sticky="E")

            containerCarro.pack(expand=True, fill='both', pady=(0,10), padx=10)

    def __click_adicionar_carros_event(self):
        JanelaCriarCarro(self)
    
    def __click_gerenciar_usuarios_event(self):
        JanelaUsuarios(self)


