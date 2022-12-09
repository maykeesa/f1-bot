import keys

#Dicts
construtores = keys.construtores()

#Quantidades
qtdConstrutores = keys.qtdConstrutores()

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