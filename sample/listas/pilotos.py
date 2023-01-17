import sample.keys as keys

#Dicts
pilotos = keys.pilotos()

#Quantidades
qtdPilotos = keys.qtdPilotos()

# PILOTOS

#Lista dos nomes dos atuais pilotos do campeonato de f1 - ex: Max
def nome():
	listPilotos = []

	for i in pilotos[0:qtdPilotos]:
		listPilotos.append(i['givenName'])

	return listPilotos

#Lista dos sobrenomes dos atuais pilotos do campeonato de F1 - ex: Verstappen
def sobrenome():
	listPilotosFamily = []

	for i in pilotos[0:qtdPilotos]:
		listPilotosFamily.append(i['familyName'])

	return listPilotosFamily

#Lista dos code dos atuais pilotos do campeonato de F1 - ex: VER
def codigo():
	listPilotosCode = []

	for i in pilotos[0:qtdPilotos]:
		listPilotosCode.append(i['code'])

	return listPilotosCode

#Lista dos números dos atuais pilotos do campeonato de F1 - ex: 33
def numero():
	listPilotosNumber = []

	# Caso o número do piloto seja apenas 1 dígitos, ele adiciona um 0 na frente do dígito
	for i in pilotos[0:qtdPilotos]:

		numeroPiloto = i['permanentNumber']

		if len(str(numeroPiloto)) == 1:
			numberNovo = '%02d' % int(numeroPiloto)
			listPilotosNumber.append(numberNovo)
		else:
			listPilotosNumber.append(numeroPiloto)

	return listPilotosNumber

#Lista das nacionalidades dos atuais pilotos do compeonato de F1 - ex: Dutch
def nacionalidade():
	listPilotosNacionalidade = []

	for i in pilotos[0:qtdPilotos]:
		listPilotosNacionalidade.append(i['nationality'])

	return listPilotosNacionalidade