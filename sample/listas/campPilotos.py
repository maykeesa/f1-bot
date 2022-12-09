import keys

#Dicts
campeonatoPiloto = keys.campPilotos()

#Quantidades
qtdPilotos = keys.qtdPilotos()

# CAMPEONATO DE PILOTOS

#Lista dos nomes dos pilotos
def nome():
	listPilotosNome = []

	for i in range(qtdPilotos):
		piloto = campeonatoPiloto[i]['Driver']
		listPilotosNome.append(piloto["givenName"])

	return listPilotosNome

#Lista dos sobrenomes dos pilotos
def sobrenome():
	listPilotosSobrenome = []

	for i in range(qtdPilotos):
		piloto = campeonatoPiloto[i]['Driver']
		listPilotosSobrenome.append(piloto["familyName"])

	return listPilotosSobrenome	

#Lista dos pontos dos pilotos
def pontos():
	listPilotosPontos = []

	for i in range(qtdPilotos):
		pilotoPontos = campeonatoPiloto[i]['points']
		listPilotosPontos.append(pilotoPontos)

	return listPilotosPontos	

#Lista da quantidade de vitórias dos pilotos
def vitoria():
	listPilotosVitoria = []

	for i in range(qtdPilotos):
		pilotoWins = campeonatoPiloto[i]['wins']
		listPilotosVitoria.append(pilotoWins)

	return listPilotosVitoria

#Lista dos construtores dos pilotos
def construtores():
	listPilotosConstrutores = []

	for i in range(qtdPilotos):
		pilotoConstrutor = campeonatoPiloto[i]['Constructors']
		listPilotosConstrutores.append(pilotoConstrutor[0]["name"])

	return listPilotosConstrutores

#Lista da quantidade de pilotos no campeonato
def posicao():
	listPilotosPos = []

	for i in range(qtdPilotos):
		listPilotosPos.append(i + 1)

	return listPilotosPos