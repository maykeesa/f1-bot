from datetime import date
import requests
import json

anoAtual = date.today().year

#Datas das API's
dataConstrutores = requests.get(f'http://ergast.com/api/f1/{anoAtual}/constructors.json')
construtoresJson = dataConstrutores.json()

dataPilotos = requests.get(f'http://ergast.com/api/f1/{anoAtual}/drivers.json')
pilotosJson = dataPilotos.json()

dataCircuitos = requests.get(f'http://ergast.com/api/f1/{anoAtual}/circuits.json')
circuitosJson = dataCircuitos.json()

qtdPilotos = int(pilotosJson['MRData']["total"])
qtdConstrutores = int(construtoresJson['MRData']["total"])
qtdCircuitos = int(circuitosJson['MRData']["total"])

#Todos os retornos dessas listas estão em ordem alfabética

#Lista dos atuais construtores do campeonato de F1 - ex: Red Bull
def construtoresAtual():
	listConstrutores = []

	construtoresTabela = construtoresJson['MRData']["ConstructorTable"]
	construtores = construtoresTabela['Constructors']

	for i in construtores[0:qtdConstrutores]:
		listConstrutores.append(i['name'])
	
	return listConstrutores

#Lista da nacionalidade dos atuais construtores de F1 - ex: Austrian
def nacionalidadeConstrutores():
	listNacionalidadeConst = []

	construtoresTabela = construtoresJson['MRData']["ConstructorTable"]
	construtores = construtoresTabela['Constructors']

	for i in construtores[0:qtdConstrutores]:	
		listNacionalidadeConst.append(i['nationality'])

	return listNacionalidadeConst

#Lista dos atuais pilotos do campeonato de f1 - ex: Max
def pilotosName():
	listPilotos = []

	pilotosTabela = pilotosJson['MRData']["DriverTable"]
	pilotos = pilotosTabela['Drivers']

	for i in pilotos[0:qtdPilotos]:
		listPilotos.append(i['givenName'])

	return listPilotos

#Lista dos sobrenomes dos atuais pilotos do campeonato de F1 - ex: Verstappen
def pilotosFamilyName():
	listPilotosFamily = []

	pilotosTabela = pilotosJson['MRData']["DriverTable"]
	pilotos = pilotosTabela['Drivers']

	for i in pilotos[0:qtdPilotos]:
		listPilotosFamily.append(i['familyName'])

	return listPilotosFamily

#Lista dos code dos atuais pilotos do campeonato de F1 - ex: VER
def pilotosCode():
	listPilotosCode = []

	pilotosTabela = pilotosJson['MRData']["DriverTable"]
	pilotos = pilotosTabela['Drivers']

	for i in pilotos[0:qtdPilotos]:
		listPilotosCode.append(i['code'])

	return listPilotosCode

#Lista dos números dos atuais pilotos do campeonato de F1 - ex: 33
def pilotosNumber():
	listPilotosNumber = []

	pilotosTabela = pilotosJson['MRData']["DriverTable"]
	pilotos = pilotosTabela['Drivers']

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
def pilotosNacionalidade():
	listPilotosNacionalidade = []

	pilotosTabela = pilotosJson['MRData']["DriverTable"]
	pilotos = pilotosTabela['Drivers']

	for i in pilotos[0:qtdPilotos]:
		listPilotosNacionalidade.append(i['nationality'])

	return listPilotosNacionalidade

#Lista dos circuitos atuais do campeonato de F1 - ex: Sâo Paulo
def circuitosAtual():
	listCircuitos = []

	circuitosTabela = circuitosJson['MRData']["CircuitTable"]
	circuitos = circuitosTabela['Circuits']

	for i in circuitos[0:qtdCircuitos]:
		circuito = i['Location']["locality"]
		listCircuitos.append(f'GP of {circuito}')

	return listCircuitos

#Lista das localidados dos atuais circuitos do campeonato de F1 - ex: Brazil
def circuitosLocalidade():
	listCircuitosLoc = []

	circuitosTabela = circuitosJson['MRData']["CircuitTable"]
	circuitos = circuitosTabela['Circuits']

	for i in circuitos[0:qtdCircuitos]:
		listCircuitosLoc.append(i['Location']["country"])

	return listCircuitosLoc

if __name__ == "__main__":
	print(circuitosLocalidade())