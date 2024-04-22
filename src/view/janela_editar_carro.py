import tkinter as Tk

from controller.janela_editar_carro_controller import JanelaEditarCarroController 
from view.janela_formulario_carro import JanelaFormularioCarro

class JanelaEditarCarro(JanelaFormularioCarro):
	def __init__(self, gerenciador, carro):
		super().__init__(JanelaEditarCarroController(gerenciador, self))

		self.carro = carro
		self.title("Editar carro")
		self.resizable(False,False)

		self.inicializar(
			cor=carro.cor,
			placa=carro.placa,
			modelo=carro.modelo,
			taxaDia=str(carro.taxa_dia) if carro.taxa_dia != None else "",
			taxaHora=str(carro.taxa_hora) if carro.taxa_hora != None else "",
		)
