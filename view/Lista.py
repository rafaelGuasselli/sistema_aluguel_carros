from PIL import Image, ImageTk
import tkinter as Tk

class Lista(Tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.photo = ImageTk.PhotoImage(Image.open("images/image.png"))
        self.containerList = Tk.Frame(self)
        self.containerList.columnconfigure((0,2,4), weight=5)
        self.containerList.columnconfigure((1,3), weight=1, minsize=30)

        # Para alugar, editar carros, editar usuarios
        self.permissions = "100" 
        self.columns = [0,2,4]
        self.__create_gidgets()
        self.containerList.pack(pady=(20,20))
        self.pack()

    def __create_gidgets(self):
        row = 0
        for i in range(21):
            containerCarro = Tk.Frame(self.containerList)
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
                Tk.Frame(self.containerList, height=30).grid(row=row+1, column=0, columnspan=2)
                row+=2

