import tkinter as Tk
from tkinter import ttk
from view.lista import Lista

class JanelaUsuarios(Tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.geometry("500x700")
        self.title("Gerenciar usuários")	
        self.addUser = Tk.Frame(self)
        Tk.Button(self.addUser, text="Adicionar usuário", command=self.__click_adicionar_usuario_event).pack(pady=10)
        self.addUser.pack()
        ttk.Separator(self, orient="horizontal").pack(fill="x", pady=(0,10))
        self.list = Lista(self)
        self.containerContent = Tk.Frame(self.list.interior)
        self.containerContent.columnconfigure(0, weight=1)
        self.__create_gidgets()
        self.containerContent.pack(padx=5, pady=5, fill=Tk.BOTH)
        self.list.pack(expand=True, fill=Tk.BOTH)
    

    def __create_gidgets(self):
        for i in range(10):
            userContainer = Tk.Frame(self.containerContent)
            userContainer.columnconfigure(0, weight=5)
            userContainer.columnconfigure(1, minsize=50, weight=1)
            Tk.Label(userContainer, text="Nome usuário"+str(i), justify="left", font=("Arial", 14, "bold") ).grid(column=0,row=0,sticky="W")
            Tk.Label(userContainer, text="Posição"+str(i), justify="left", ).grid(column=0,row=1,sticky="W")
            Tk.Button(userContainer,text="Editar", command=self.__click_editar_usuario_event).grid(column=1, row=0, sticky="WE")
            Tk.Button(userContainer,text="Excluir", command=self.__click_excluir_usuario_event).grid(column=1, row=1, sticky="WE")
            userContainer.grid(row=i, sticky="WE", pady=(0,20))


    def __click_editar_usuario_event(self):
        pass

    def __click_excluir_usuario_event(self):
        pass

    def __click_adicionar_usuario_event(self):
        pass

