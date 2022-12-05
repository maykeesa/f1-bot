import api

# Formatação da lista de !campPilotos
def campPilotos() -> list:
    listaCampPilotos = []

    qtdPilotos = len(api.campPilotoNome())
    listaCampPilotosPos = api.campPilotosPosicao()
    listaCampPilotosNome = api.campPilotoNome()
    listaCampPilotosSobrenome = api.campPilotoSobrenome()
    listaCampPilotosPontos = api.campPilotoPontos()
    listaCampPilotoConstrutores = api.campPilotoConstrutores()

    for i in range(qtdPilotos):
        listaCampPilotos.append(f'{listaCampPilotosPos[i]} - {listaCampPilotosNome[i]} {listaCampPilotosSobrenome[i]} - {listaCampPilotoConstrutores[i]} - {listaCampPilotosPontos[i]} Pontos')

    return listaCampPilotos

# Formatação da lista de !campConstrutores
def campConstrutores() -> list:

    listaCampConstrutores = []

    qtdConstrutores = len(api.campPosicaoConstrutores())
    listaCampConstrutoresPos = api.campPosicaoConstrutores()
    listaCampConstrutoresNome = api.campConstrutoresNome()
    listaCampConstrutoresPontos = api.campConstrutoresPontos()
    listaCampConstrutoresWins = api.campConstrutoresWins()

    for i in range(qtdConstrutores):
        listaCampConstrutores.append(f'{listaCampConstrutoresPos[i]} - {listaCampConstrutoresNome[i]} - {listaCampConstrutoresPontos[i]} Pontos - {listaCampConstrutoresWins[i]} Vitórias')

    return listaCampConstrutores

# Formataão da lista de !corrida
def corrida() -> list:
    listaCorrida = []

    qtdPilotos = len(api.corridaPosicao())
    listaCorridaPosicao = api.corridaPosicao()
    listaCorridaNome = api.corridaNome()
    listaCorridaSobrenome = api.corridaSobrenome()
    listaCorridaPontos = api.corridaPontos()
    listaCorridaConstrutores = api.corridaConstrutores()

    for i in range(qtdPilotos):
        listaCorrida.append(f'{listaCorridaPosicao[i]} - {listaCorridaNome[i]} {listaCorridaSobrenome[i]} - {listaCorridaConstrutores[i]} - {listaCorridaPontos[i]}')

    return listaCorrida  

# Formatação da lista de !quali
def quali() -> list:
    listaQuali = []

    qtdPilotos = len(api.qualiNome())
    listaQualiPosicao = api.corridaPosicao()
    listaQualiNome = api.qualiNome()
    listaQualiSobrenome = api.qualiSobrenome()
    listaQualiConstrutores = api.qualiConstrutores()
    listaQualiTempo = api.qualiTempo()

    for i in range(qtdPilotos):
        listaQuali.append(f'{listaQualiPosicao[i]} - {listaQualiNome[i]} {listaQualiSobrenome[i]} - {listaQualiConstrutores[i]} - {listaQualiTempo[i]}')

    return listaQuali

# Formatação da lista de !cosntrutores
def construtores() -> list:
    listaConstrutoresMain = []

    qtdConstrutores = len(api.construtoresAtual())
    listaConstrutores = api.construtoresAtual()
    listaNacionalidadeConstrutores = api.construtoresNacionalidade()

    for i in range(qtdConstrutores):
        listaConstrutoresMain.append(f'{listaConstrutores[i]} - {listaNacionalidadeConstrutores[i]}')

    return listaConstrutoresMain

# Formatação da lista de !pilotos
def pilotos() -> list:
    listaPilotos = []

    qtdPilotos = len(api.pilotosNome())
    listaPilotosNome = api.pilotosNome()
    listaPilotosCode = api.pilotosCodigo()
    listaPilotosNumber = api.pilotosNumero()
    listaPilotosFamily = api.pilotosSobrenome()
    listaPilotosNacionalidade = api.pilotosNacionalidade()

    for i in range(qtdPilotos):
        listaPilotos.append(f'{listaPilotosNumber[i]} - {listaPilotosCode[i]} - {listaPilotosNome[i]} {listaPilotosFamily[i]} - {listaPilotosNacionalidade[i]}')

    return listaPilotos

# Formatação da lista de !circuitos
def circuitos() -> list:
    listaCircuitos = []

    qtdCircuitos = len(api.circuitosAtual())
    listaCircuitosAtual = api.circuitosAtual()
    listaCircuitosLoc = api.circuitosLocalidade()

    for i in range(qtdCircuitos):
        listaCircuitos.append(f'{listaCircuitosLoc[i]} - {listaCircuitosAtual[i]}')

    return listaCircuitos

# Formatação da lista de !calendario
def calendario() -> list:
    listaCalendario = []
    
    qtdCalendario = len(api.circuitosAtual())
    listaQtdCalendario = api.calendarioQtdCorridas()
    listaCalendarioGP = api.calendarioGP()
    listaCalendarioData = api.calendarioData()

    for i in range(qtdCalendario):
        listaCalendario.append(f'{listaQtdCalendario[i]} - {listaCalendarioGP[i]} | {listaCalendarioData[i]}')

    return listaCalendario