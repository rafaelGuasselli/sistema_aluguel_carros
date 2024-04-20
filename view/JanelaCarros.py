import tkinter as Tk
from view.Lista import Lista
from view.JanelaCriarCarro import JanelaCriarCarro
from view.JanelaUsuarios import JanelaUsuarios
from PIL import Image, ImageTk

class JanelaCarros(Tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        self.photo = ImageTk.PhotoImage(Image.open("images/image.png"))
        # Alugar, editar carros, editar usuários 
        self.permissions = "111"
        self.columns = [0,2,4]
        self.__create_gidgets()
        self.mainloop()

    def __create_gidgets(self):
        superior = Tk.Frame(self, highlightbackground="blue", highlightthickness=1)
        if (self.permissions[2] == '1'):
            Tk.Button(superior, text="Gerenciar usuários", command=self.__click_gerenciar_usuarios_event).pack(side="right", padx=(0,20), pady=10)
        
        if (self.permissions[1] == '1'):
            Tk.Button(superior, text="Adicionar carros", command=self.__click_adicionar_carros_event).pack(side="right", padx=(0,20), pady=10)
        
        Tk.Label(superior, text="Veículos", font=("Arial", 18, "bold")).pack(side="left", padx=(10,0))
        
        # Cria o container para a listagem de carros
        central = Tk.Frame(self)

        # Cria a lista de carros
        lista = Lista(central)
        self.containerList = Tk.Frame(lista.interior)
        self.containerList.columnconfigure((0,2,4), weight=5)
        self.containerList.columnconfigure((1,3), weight=1, minsize=30)
        self.__create_cars(self.containerList)
        self.containerList.pack()
        lista.pack(expand=True, fill=Tk.BOTH)
        
        # Renderiza central e superior
        central.grid(sticky="WE",row=1, column=0)
        superior.grid(row=0, sticky="NSWE")
    
    # A partir de informacoes varios elementos carros
    def __create_cars(self, containerList):
        row = 0
        for i in range(21):
            containerCarro = Tk.Frame(containerList)
            containerCarro.columnconfigure(tuple(range(10)), weight=1)
            containerCarro.rowconfigure((0,2,3), weight=1)
            containerCarro.rowconfigure(1, weight=5)

            Tk.Label(containerCarro, text="Modelo " + str(i)).grid(column=0, columnspan=11, row=0, sticky="WE")
            containerImagemCarro = Tk.Frame(containerCarro)
            imagem = Tk.Label(containerImagemCarro, text="teste", image=self.photo, compound="bottom")
            imagem.pack()
            containerImagemCarro.grid(column=0, columnspan=11, row=1)
            Tk.Label(containerCarro, text="Breve descrição").grid(column=0, columnspan=11, row=2, sticky="WE")

            botaoAlugar = Tk.Button(containerCarro, text="Alugar", )
            botaoRemover = Tk.Button(containerCarro, text="Remover")
            botaoEditar = Tk.Button(containerCarro, text="Editar")

            cont = self.permissions[0:2].count('1')
            if (cont == 2 and self.permissions[1] == '1'):
                cont+=1
            quantColunas = 10 // cont
            comeco = 0
            if quantColunas == 10:
                quantColunas+=1
            colocadas = 0

            if (self.permissions[0] == '1'):
                botaoAlugar.grid(row=3, column=comeco, columnspan=quantColunas, sticky="WE", pady=10)
                colocadas+=1
                comeco = quantColunas+1

            if (self.permissions[1] == '1'):
                botaoRemover.grid(row=3, column=comeco, columnspan=quantColunas, sticky="WE", pady=10)
                colocadas+=1    
                comeco += quantColunas+1
                botaoEditar.grid(row=3, column=comeco, columnspan=quantColunas, sticky="WE", pady=10)

            containerCarro.grid(row=row, column=self.columns[i%3])
            if (i + 1) % 3 == 0:
                Tk.Frame(containerList, height=30).grid(row=row+1, column=0, columnspan=2)
                row+=2

    def __click_adicionar_carros_event(self):
        JanelaCriarCarro(self)
    
    def __click_gerenciar_usuarios_event(self):
        JanelaUsuarios(self)


