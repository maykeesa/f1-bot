import keys
from datetime import datetime

#Quantidades de Construtores, Pilotos e Circuitos para utlizar nas funções
qtdPilotos = keys.qtdPilotos()
qtdConstrutores = keys.qtdConstrutores()
qtdCircuitos = keys.qtdCircuitos()
qtdPilotosCorrida = keys.qtdPilotosCorrida()
qtdPilotosQuali = keys.qtdPilotosQuali()

#Chaves dos dicionários de Construtores, Pilotos e Circuitos
construtores = keys.construtores()
pilotos = keys.pilotos()
circuitos = keys.circuitos()
corridaResultado = keys.corridaResultado()
qualiResultado = keys.quali()
calendario = keys.calendario()
campeonatoCons = keys.campConstrutores()
campeonatoPiloto = keys.campPilotos()

# CONSTRUTORES

#Lista dos atuais construtores do campeonato de F1 - ex: Red Bull
def construtoresAtual():
	listConstrutores = []

	for i in construtores[0:qtdConstrutores]:
		listConstrutores.append(i['name'])
	
	return listConstrutores

#Lista da nacionalidade dos atuais construtores de F1 - ex: Austrian
def construtoresNacionalidade():
	listNacionalidadeConst = []

	for i in construtores[0:qtdConstrutores]:	
		listNacionalidadeConst.append(i['nationality'])

	return listNacionalidadeConst

# PILOTOS

#Lista dos nomes dos atuais pilotos do campeonato de f1 - ex: Max
def pilotosNome():
	listPilotos = []

	for i in pilotos[0:qtdPilotos]:
		listPilotos.append(i['givenName'])

	return listPilotos

#Lista dos sobrenomes dos atuais pilotos do campeonato de F1 - ex: Verstappen
def pilotosSobrenome():
	listPilotosFamily = []

	for i in pilotos[0:qtdPilotos]:
		listPilotosFamily.append(i['familyName'])

	return listPilotosFamily

#Lista dos code dos atuais pilotos do campeonato de F1 - ex: VER
def pilotosCodigo():
	listPilotosCode = []

	for i in pilotos[0:qtdPilotos]:
		listPilotosCode.append(i['code'])

	return listPilotosCode

#Lista dos números dos atuais pilotos do campeonato de F1 - ex: 33
def pilotosNumero():
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
def pilotosNacionalidade():
	listPilotosNacionalidade = []

	for i in pilotos[0:qtdPilotos]:
		listPilotosNacionalidade.append(i['nationality'])

	return listPilotosNacionalidade

# CIRCUITOS

#Lista dos circuitos atuais do campeonato de F1 - ex: Sâo Paulo
def circuitosAtual():
	listCircuitos = []

	for i in circuitos[0:qtdCircuitos]:
		circuito = i['Location']["locality"]
		listCircuitos.append(f'GP of {circuito}')

	return listCircuitos

#Lista das localidados dos atuais circuitos do campeonato de F1 - ex: Brazil
def circuitosLocalidade():
	listCircuitosLoc = []

	for i in circuitos[0:qtdCircuitos]:
		listCircuitosLoc.append(i['Location']["country"])

	return listCircuitosLoc

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

# QUALI

#Lista dos nomes dos pilotos por ordem da ultima qualificacao
def qualiNome():
	listQualiNome = []

	for i in range(qtdPilotosQuali):
		qualiPilotos = qualiResultado[i]['Driver']
		listQualiNome.append(qualiPilotos['givenName'])

	return listQualiNome	

#Lista dos sobrenomes dos pilotos por ordem da ultima qualificacao
def qualiSobrenome():
	listQualiSobrenome = []

	for i in range(qtdPilotosQuali):
		qualiPilotos = qualiResultado[i]['Driver']
		listQualiSobrenome.append(qualiPilotos['familyName'])

	return listQualiSobrenome

#Lista dos construtores dos pilotos por ordem da ultima qualificacao
def qualiConstrutores():
	listQualiConstrutores = []

	for i in range(qtdPilotosQuali):
		qualiPilotos = qualiResultado[i]['Constructor']
		listQualiConstrutores.append(qualiPilotos['name'])

	return listQualiConstrutores	

#Lista do tempos dos pilotos por ordem da ultima qualificação 
def qualiTempo():
	listQualiTempo = []

	for i in range(10):
		listQualiTempo.append(qualiResultado[i]['Q3'])
	for i in range(5):
		listQualiTempo.append(qualiResultado[i + 10]['Q2'])
	for i in range(5):
		listQualiTempo.append(qualiResultado[i + 15]['Q1'])

	return listQualiTempo		

# CALENDARIO 

#Lista dos nomes dos GP's do calendario
def calendarioGP():
	listCalendarioGP = []

	for i in range(qtdCircuitos):
		calendarioResultado = calendario[i]
		listCalendarioGP.append(calendarioResultado['raceName'])

	return listCalendarioGP

#Lista das datas dos GP's do calendario
def calendarioData():
	listCalendarioData = []

	for i in range(qtdCircuitos):
		calendarioResultado = calendario[i]
		dataAtual = str(calendarioResultado['date'])
		dataAno = dataAtual[0:4]
		dataMes = dataAtual[5:7]
		dataDia = dataAtual[8:10]

		dataFormatada = datetime.strptime(f"{dataAno}/{dataMes}/{dataDia}", "%Y/%m/%d").strftime("%d-%m-%Y")

		listCalendarioData.append(dataFormatada)

	return listCalendarioData

#Lista da quantidade de corridas
def calendarioQtdCorridas():
	listCorridas = []

	for i in range(qtdCircuitos):
		listCorridas.append(i + 1)

	return listCorridas

# CAMPEONATO DE CONSTRUTORES

#Lista de 1 a 10
def campPosicaoConstrutores():
	listPosicao = []

	for i in range(qtdConstrutores):
		listPosicao.append(i + 1)

	return listPosicao

#Lista dos nomes dos construtores em ordem
def campConstrutoresNome():
	listConstrutores = []

	for i in range(qtdConstrutores):
		construtor = campeonatoCons[i]['Constructor']
		listConstrutores.append(construtor["name"])

	return listConstrutores

#Lista dos pontos dos contrutores
def campConstrutoresPontos():
	listConstrutoresPontos = []

	for i in range(qtdConstrutores):
		listConstrutoresPontos.append(campeonatoCons[i]['points'])

	return listConstrutoresPontos

#Lista de vitorias dos contrutores
def campConstrutoresWins():
	listConstrutoresWins = []

	for i in range(qtdConstrutores):
		listConstrutoresWins.append(campeonatoCons[i]['wins'])

	return listConstrutoresWins

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

	qtdPilotosCamp = int(campeonatoPiJson['MRData']["total"])

	for i in range(qtdPilotosCamp):
		listPilotosPos.append(i + 1)

	return listPilotosPos

if __name__ == "__main__":
	print(type(construtoresJson))