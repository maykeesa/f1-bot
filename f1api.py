import requests
import json

dataConstrutores = requests.get('http://ergast.com/api/f1/2022/constructors.json')
construtoresJson = dataConstrutores.json()

dataPilotos = requests.get('http://ergast.com/api/f1/2022/drivers.json')
pilotosJson = dataPilotos.json()

# Lista dos atuais construtores do campeonato de F1 - ex: Red Bull
def construtoresAtual():

	listConstrutores = []

	construtoresTabela = construtoresJson['MRData']["ConstructorTable"]
	construtores = construtoresTabela['Constructors']

	for i in construtores[:10]:
		listConstrutores.append(i['name'])
	
	return listConstrutores

#Lista da nacionalidade dos atuais construtores de F1 - ex: Austrian
def nacionalidadeConstrutores():

	listNacionalidadeConst = []

	construtoresTabela = construtoresJson['MRData']["ConstructorTable"]
	construtores = construtoresTabela['Constructors']

	for i in construtores[:10]:	
		listNacionalidadeConst.append(i['nationality'])

	return listNacionalidadeConst

#Lista dos atuais pilotos do campeonato de f1 - ex: Max
def pilotosName():

	listPilotos = []

	pilotosTabela = pilotosJson['MRData']["DriverTable"]
	pilotos = pilotosTabela['Drivers']

	for i in pilotos[0:21]:
		listPilotos.append(i['givenName'])

	return listPilotos

#Lista dos sobrenomes dos atuais pilotos do campeonato de F1 - ex: Verstappen
def pilotosFamilyName():
	listPilotosFamily = []

	pilotosTabela = pilotosJson['MRData']["DriverTable"]
	pilotos = pilotosTabela['Drivers']

	for i in pilotos[0:21]:
		listPilotosFamily.append(i['familyName'])

	return listPilotosFamily

#Lista dos code dos atuais pilotos do campeonato de F1 - ex: VER
def pilotosCode():

	listPilotosCode = []

	pilotosTabela = pilotosJson['MRData']["DriverTable"]
	pilotos = pilotosTabela['Drivers']

	for i in pilotos[0:21]:
		listPilotosCode.append(i['code'])

	return listPilotosCode

#Lista dos números dos atuais pilotos do campeonato de F1 - ex: 33
def pilotosNumber():
	listPilotosNumber = []

	pilotosTabela = pilotosJson['MRData']["DriverTable"]
	pilotos = pilotosTabela['Drivers']

	# Caso o número do piloto seja apenas 1 dígitos, ele adiciona um 0 na frente do dígito
	for i in pilotos[0:21]:
		if len(str(i['permanentNumber'])) == 1:
			numberNovo = '%02d' % int(i['permanentNumber'])
			listPilotosNumber.append(numberNovo)
		else:
			listPilotosNumber.append(i['permanentNumber'])

	return listPilotosNumber

#Lita das nacionalidades dos atuais pilotos do compeonato de F1 - ex: Dutch
def pilotosNacionalidade():
	listPilotosNacionalidade = []

	pilotosTabela = pilotosJson['MRData']["DriverTable"]
	pilotos = pilotosTabela['Drivers']

	for i in pilotos[0:21]:
		listPilotosNacionalidade.append(i['nationality'])

	return listPilotosNacionalidade
	
if __name__ == '__main__':
	pilotosNumber()