from tkinter import messagebox

class JanelaPopup:
	def __init__(self, titulo, mensagem):
		messagebox.showinfo(titulo, mensagem)