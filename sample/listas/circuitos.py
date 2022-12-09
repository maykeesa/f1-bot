import keys

#Dicts
circuitos = keys.circuitos()

#Quantidades
qtdCircuitos = keys.qtdCircuitos()

# CIRCUITOS

#Lista dos circuitos atuais do campeonato de F1 - ex: Sâo Paulo
def nome():
	listCircuitos = []

	for i in circuitos[0:qtdCircuitos]:
		circuito = i['Location']["locality"]
		listCircuitos.append(f'GP of {circuito}')

	return listCircuitos

#Lista das localidados dos atuais circuitos do campeonato de F1 - ex: Brazil
def localidade():
	listCircuitosLoc = []

	for i in circuitos[0:qtdCircuitos]:
		listCircuitosLoc.append(i['Location']["country"])

	return listCircuitosLoc
