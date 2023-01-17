import sample.keys as keys
from datetime import datetime

#Dicts
calendario = keys.calendario()

#Quantidades
qtdCalendario = keys.qtdCalendario()

# CALENDARIO 

#Lista dos nomes dos GP's do calendario
def calendarioGP():
	listCalendarioGP = []

	for i in range(qtdCalendario):
		calendarioResultado = calendario[i]
		listCalendarioGP.append(calendarioResultado['raceName'])

	return listCalendarioGP

#Lista das datas dos GP's do calendario
def datas():
	listCalendarioData = []

	for i in range(qtdCalendario):
		calendarioResultado = calendario[i]
		dataAtual = str(calendarioResultado['date'])
		dataAno = dataAtual[0:4]
		dataMes = dataAtual[5:7]
		dataDia = dataAtual[8:10]

		dataFormatada = datetime.strptime(f"{dataAno}/{dataMes}/{dataDia}", "%Y/%m/%d").strftime("%d-%m-%Y")

		listCalendarioData.append(dataFormatada)

	return listCalendarioData

#Lista da quantidade de corridas
def qtdCorridas():
	listCorridas = []

	for i in range(qtdCalendario):
		listCorridas.append(i + 1)

	return listCorridas