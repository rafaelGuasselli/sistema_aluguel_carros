import tkinter as Tk

from controller.janela_criar_carro_controller import JanelaCriarCarroController 
from view.janela_formulario_carro import JanelaFormularioCarro

class JanelaCriarCarro(JanelaFormularioCarro):
	def __init__(self, gerenciador):
		super().__init__(JanelaCriarCarroController(gerenciador, self))

		self.carro = None
		self.title("Criar carro")
		self.resizable(False,False)

		self.inicializar(
			cor="",
			placa="",
			modelo="",
			taxaDia="",
			taxaHora="",
		)
