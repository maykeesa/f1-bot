import keys

#Dicts
corridaResultado = keys.corridaResultado()

#Quantidades
qtdPilotosCorrida = keys.qtdPilotosCorrida()

# CORRIDA

#Função que retorna uma string do último GP
def corridaGP() -> str:
	corridaGP = str(keys.corridaNome())

	return corridaGP

#Lista dos nomes dos pilotos por ordem de chegada da ultima corrida
def corridaNome():
	listCorridaNome = []

	for i in range(qtdPilotosCorrida):
		corridaPilotos = corridaResultado[i]['Driver']
		listCorridaNome.append(corridaPilotos['givenName'])

	return listCorridaNome

#Lista dos nomes dos pilotos por ordem de chegada da ultima corrida
def corridaSobrenome():
	listCorridaSobrenome = []

	for i in range(qtdPilotosCorrida):
		corridaPilotos = corridaResultado[i]['Driver']
		listCorridaSobrenome.append(corridaPilotos['familyName'])

	return listCorridaSobrenome

#Lista dos construtores dos pilotos por ordem de chegada
def corridaConstrutores():
	listCorridaConstrutores = []

	for i in range(qtdPilotosCorrida):
		corridaPilotos = corridaResultado[i]['Constructor']
		listCorridaConstrutores.append(corridaPilotos['name'])

	return listCorridaConstrutores	

#Lista das pontuações dos pilotos por ordem de chegada da ultima corrida
def corridaPontos():
	listCorridaPontos = []

	for i in range(qtdPilotosCorrida):
		corridaPontos = corridaResultado[i]['points']
		listCorridaPontos.append(corridaPontos)

	return listCorridaPontos

#Lista de 1 a 20
def corridaPosicao():
	listPosicao = []

	for i in range(qtdPilotosCorrida):
		listPosicao.append(i + 1)

	return listPosicao