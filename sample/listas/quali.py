import keys

#Dicts
qualiResultado = keys.quali()

#Quantidades
qtdPilotosQuali = keys.qtdPilotosQuali()

# QUALI

#Lista dos nomes dos pilotos por ordem da ultima qualificacao
def nome():
	listQualiNome = []

	for i in range(qtdPilotosQuali):
		qualiPilotos = qualiResultado[i]['Driver']
		listQualiNome.append(qualiPilotos['givenName'])

	return listQualiNome	

#Lista dos sobrenomes dos pilotos por ordem da ultima qualificacao
def sobrenome():
	listQualiSobrenome = []

	for i in range(qtdPilotosQuali):
		qualiPilotos = qualiResultado[i]['Driver']
		listQualiSobrenome.append(qualiPilotos['familyName'])

	return listQualiSobrenome

#Lista dos construtores dos pilotos por ordem da ultima qualificacao
def construtores():
	listQualiConstrutores = []

	for i in range(qtdPilotosQuali):
		qualiPilotos = qualiResultado[i]['Constructor']
		listQualiConstrutores.append(qualiPilotos['name'])

	return listQualiConstrutores	

#Lista do tempos dos pilotos por ordem da ultima qualificação 
def tempo():
	listQualiTempo = []

	for i in range(10):
		listQualiTempo.append(qualiResultado[i]['Q3'])
	for i in range(5):
		listQualiTempo.append(qualiResultado[i + 10]['Q2'])
	for i in range(5):
		listQualiTempo.append(qualiResultado[i + 15]['Q1'])

	return listQualiTempo		