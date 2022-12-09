import keys

#Dicts
campeonatoCons = keys.campConstrutores()

#Quantidades
qtdConstrutores = keys.qtdConstrutores()

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