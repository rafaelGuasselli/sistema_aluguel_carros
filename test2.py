from model.CarroMapper import CarroMapper
from model.Carro import Carro

db = CarroMapper()
carro = Carro(1)
carro.modelo = "Prius"
carro.cor = "Vermelho"
carro.multa = 50
carro.placa = "abc123"
carro.taxa_dia = 200
carro.estimativa_devolucao = None

db.delete(carro)
carros = db.select()

for carro in carros:
	print(carro.modelo)
	print(carro.cor)
	print(carro.taxa_dia)
	print("-------------")