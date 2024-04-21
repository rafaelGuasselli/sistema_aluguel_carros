from tkinter import messagebox

class JanelaErro:
	def __init__(self, mensagem):
		messagebox.showerror("Erro", mensagem)