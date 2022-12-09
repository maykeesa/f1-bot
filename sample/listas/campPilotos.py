import keys

#Dicts
campeonatoPiloto = keys.campPilotos()

#Quantidades
qtdPilotos = keys.qtdPilotos()

# CAMPEONATO DE PILOTOS

#Lista dos nomes dos pilotos
def campPilotoNome():
	listPilotosNome = []

	for i in range(qtdPilotos):
		piloto = campeonatoPiloto[i]['Driver']
		listPilotosNome.append(piloto["givenName"])

	return listPilotosNome

#Lista dos sobrenomes dos pilotos
def campPilotoSobrenome():
	listPilotosSobrenome = []

	for i in range(qtdPilotos):
		piloto = campeonatoPiloto[i]['Driver']
		listPilotosSobrenome.append(piloto["familyName"])

	return listPilotosSobrenome	

#Lista dos pontos dos pilotos
def campPilotoPontos():
	listPilotosPontos = []

	for i in range(qtdPilotos):
		pilotoPontos = campeonatoPiloto[i]['points']
		listPilotosPontos.append(pilotoPontos)

	return listPilotosPontos	

#Lista da quantidade de vitórias dos pilotos
def campPilotoVitoria():
	listPilotosVitoria = []

	for i in range(qtdPilotos):
		pilotoWins = campeonatoPiloto[i]['wins']
		listPilotosVitoria.append(pilotoWins)

	return listPilotosVitoria

#Lista dos construtores dos pilotos
def campPilotoConstrutores():
	listPilotosConstrutores = []

	for i in range(qtdPilotos):
		pilotoConstrutor = campeonatoPiloto[i]['Constructors']
		listPilotosConstrutores.append(pilotoConstrutor[0]["name"])

	return listPilotosConstrutores

#Lista da quantidade de pilotos no campeonato
def campPilotosPosicao():
	listPilotosPos = []

	for i in range(qtdPilotos):
		listPilotosPos.append(i + 1)

	return listPilotosPos