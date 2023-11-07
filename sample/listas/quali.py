import sample.keys as keys

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

	listaQ3 = qualiResultado[0:10]
	listaQ2 = qualiResultado[10:15]
	listaQ1 = qualiResultado[15:20]

	for i in listaQ3:
		try:
			listQualiTempo.append(i['Q3'])
		except:
			listQualiTempo.append(i['Q2'])
	for i in listaQ2:
		try: 
			listQualiTempo.append(i['Q2'])
		except:
			listQualiTempo.append(i['Q1'])
	for i in listaQ1:
		try:
			listQualiTempo.append(i['Q1'])
		except:
			listQualiTempo.append("DNF")
		
	return listQualiTempo
