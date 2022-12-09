import sys

sys.path.insert(0, "./sample/listas")

import keys
import quali
import corrida
import pilotos
import circuitos
import calendario
import campPilotos
import construtores
import campConstrutores

# Formatação da lista de !campPilotos
def campPilotosComando() -> list:
    listaCampPilotos = []

    qtdPilotos = keys.qtdPilotos()
    listaCampPilotosPos = campPilotos.campPilotosPosicao()
    listaCampPilotosNome = campPilotos.campPilotoNome()
    listaCampPilotosSobrenome = campPilotos.campPilotoSobrenome()
    listaCampPilotosPontos = campPilotos.campPilotoPontos()
    listaCampPilotoConstrutores = campPilotos.campPilotoConstrutores()

    for i in range(qtdPilotos):
        listaCampPilotos.append(f'{listaCampPilotosPos[i]} - {listaCampPilotosNome[i]} {listaCampPilotosSobrenome[i]} - {listaCampPilotoConstrutores[i]} - {listaCampPilotosPontos[i]} Pontos')

    return listaCampPilotos

# Formatação da lista de !campConstrutores
def campConstrutoresComando() -> list:

    listaCampConstrutores = []

    qtdConstrutores = keys.qtdConstrutores()
    listaCampConstrutoresPos = campConstrutores.campPosicaoConstrutores()
    listaCampConstrutoresNome = campConstrutores.campConstrutoresNome()
    listaCampConstrutoresPontos = campConstrutores.campConstrutoresPontos()
    listaCampConstrutoresWins = campConstrutores.campConstrutoresWins()

    for i in range(qtdConstrutores):
        listaCampConstrutores.append(f'{listaCampConstrutoresPos[i]} - {listaCampConstrutoresNome[i]} - {listaCampConstrutoresPontos[i]} Pontos - {listaCampConstrutoresWins[i]} Vitórias')

    return listaCampConstrutores

# Formataão da lista de !corrida
def corridaComando() -> list:
    listaCorrida = []

    qtdPilotos = keys.qtdPilotosCorrida()
    listaCorridaPosicao = corrida.corridaPosicao()
    listaCorridaNome = corrida.corridaNome()
    listaCorridaSobrenome = corrida.corridaSobrenome()
    listaCorridaConstrutores = corrida.corridaConstrutores()
    listaCorridaPontos = corrida.corridaPontos()

    for i in range(qtdPilotos):
        listaCorrida.append(f'{listaCorridaPosicao[i]} - {listaCorridaNome[i]} {listaCorridaSobrenome[i]} - {listaCorridaConstrutores[i]} - {listaCorridaPontos[i]}')

    return listaCorrida  

# Formatação da lista de !quali
def qualiComando() -> list:
    listaQuali = []

    qtdPilotos = keys.qtdPilotosQuali()
    listaQualiPosicao = corrida.corridaPosicao()
    listaQualiNome = quali.qualiNome()
    listaQualiSobrenome = quali.qualiSobrenome()
    listaQualiConstrutores = quali.qualiConstrutores()
    listaQualiTempo = quali.qualiTempo()

    for i in range(qtdPilotos):
        listaQuali.append(f'{listaQualiPosicao[i]} - {listaQualiNome[i]} {listaQualiSobrenome[i]} - {listaQualiConstrutores[i]} - {listaQualiTempo[i]}')

    return listaQuali

# Formatação da lista de !cosntrutores
def construtoresComando() -> list:
    listaConstrutoresMain = []

    qtdConstrutores = keys.qtdConstrutores()
    listaConstrutores = construtores.construtoresAtual()
    listaNacionalidadeConstrutores = construtores.construtoresNacionalidade()

    for i in range(qtdConstrutores):
        listaConstrutoresMain.append(f'{listaConstrutores[i]} - {listaNacionalidadeConstrutores[i]}')

    return listaConstrutoresMain

# Formatação da lista de !pilotos
def pilotosComando() -> list:
    listaPilotos = []

    qtdPilotos = keys.qtdPilotos()
    listaPilotosNome = pilotos.pilotosNome()
    listaPilotosCode = pilotos.pilotosCodigo()
    listaPilotosNumber = pilotos.pilotosNumero()
    listaPilotosFamily = pilotos.pilotosSobrenome()
    listaPilotosNacionalidade = pilotos.pilotosNacionalidade()

    for i in range(qtdPilotos):
        listaPilotos.append(f'{listaPilotosNumber[i]} - {listaPilotosCode[i]} - {listaPilotosNome[i]} {listaPilotosFamily[i]} - {listaPilotosNacionalidade[i]}')

    return listaPilotos

# Formatação da lista de !circuitos
def circuitosComando() -> list:
    listaCircuitos = []

    qtdCircuitos = keys.qtdCircuitos()
    listaCircuitosAtual = circuitos.circuitosAtual()
    listaCircuitosLoc = circuitos.circuitosLocalidade()

    for i in range(qtdCircuitos):
        listaCircuitos.append(f'{listaCircuitosLoc[i]} - {listaCircuitosAtual[i]}')

    return listaCircuitos

# Formatação da lista de !calendario
def calendarioComando() -> list:
    listaCalendario = []
    
    qtdCalendario = keys.qtdCalendario()
    listaQtdCalendario = calendario.calendarioQtdCorridas()
    listaCalendarioGP = calendario.calendarioGP()
    listaCalendarioData = calendario.calendarioData()

    for i in range(qtdCalendario):
        listaCalendario.append(f'{listaQtdCalendario[i]} - {listaCalendarioGP[i]} | {listaCalendarioData[i]}')

    return listaCalendario