import tkinter as Tk
from view.lista import Lista
from view.janela_criar_carro import JanelaCriarCarro
from view.janela_usuario import JanelaUsuarios
from view.janela_aluga import JanelaAluga

class JanelaCarros(Tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        # Alugar, editar carros, editar usuários 
        self.columns = [0,2,4]
        self.__create_gidgets(6)
        self.bind("<MouseWheel>", self.lista._on_mousewheel)
        self.bind("<Button-4>", self.lista._on_mousewheel)
        self.bind("<Button-5>", self.lista._on_mousewheel)
        self.mainloop()


    def __create_gidgets(self, permissions):
        superior = Tk.Frame(self, highlightbackground="blue", highlightthickness=1)
        if (permissions & 1 << 2):
            Tk.Button(superior, text="Gerenciar usuários", command=self.__click_gerenciar_usuarios_event).pack(side="right", padx=(0,20), pady=10)
        
        if (permissions & 1 << 1):
            Tk.Button(superior, text="Adicionar carros", command=self.__click_adicionar_carros_event).pack(side="right", padx=(0,20), pady=10)
        
        Tk.Label(superior, text="Veículos", font=("Arial", 18, "bold")).pack(side="left", padx=(10,0))
        
        # Cria a lista de carros
        self.lista = Lista(self)
        self.containerList = self.lista.interior
        self.__create_cars(self.containerList, permissions)

        # Renderiza central e superior
        self.lista.grid(sticky="WE",row=1, column=0)
        superior.grid(row=0, sticky="NSWE")
    
    # A partir de informacoes varios elementos carros
    def __create_cars(self, containerList, permissions):
        for i in range(21):
            containerCarro = Tk.Frame(containerList)
            containerCarro.columnconfigure(0, weight=3)
            containerCarro.columnconfigure(1, weight=2)

            Tk.Label(containerCarro, text="Modelo " + str(i), justify="left").grid(column=0, row=0, sticky="W")

            containerButtons = Tk.Frame(containerCarro)

            botaoAlugar = Tk.Button(containerButtons,command=self.__click_button_alugar_event, text="Alugar")
            botaoRemover = Tk.Button(containerButtons, text="Remover")
            botaoEditar = Tk.Button(containerButtons, text="Editar")


            if (permissions & 1 << 0):
                botaoAlugar.pack(side="right", padx=10)


            if (permissions & 1 << 1):
                botaoEditar.pack(side="right", padx=(10,0))
                botaoRemover.pack(side="right")

            containerButtons.grid(row=0, column=1, sticky="E")

            containerCarro.pack(expand=True, fill='both', pady=(0,10), padx=10)

    def __click_adicionar_carros_event(self):
        JanelaCriarCarro(self)
    
    def __click_gerenciar_usuarios_event(self):
        JanelaUsuarios(self)

    def __click_button_alugar_event(self):
        JanelaAluga(self)

