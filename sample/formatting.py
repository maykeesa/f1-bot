import sys

sys.path.insert(0, "./sample/listas")

import sample.keys as keys
import sample.listas.quali as quali
import sample.listas.corrida as corrida
import sample.listas.pilotos as pilotos
import sample.listas.circuitos as circuitos
import sample.listas.calendario as calendario
import sample.listas.campPilotos as campPilotos
import sample.listas.construtores as construtores
import sample.listas.campConstrutores as campConstrutores

# Formatação da lista de !campPilotos
def campPilotosComando() -> list:
    listaCampPilotos = []

    qtdPilotos = keys.qtdPilotos()
    listaPos = campPilotos.posicao()
    listaNome = campPilotos.nome()
    listaSobrenome = campPilotos.sobrenome()
    listaConstrutores = campPilotos.construtores()
    listaPontos = campPilotos.pontos()

    for i in range(qtdPilotos):
        listaCampPilotos.append(f'{listaPos[i]} - {listaNome[i]} {listaSobrenome[i]} - {listaConstrutores[i]} - {listaPontos[i]} Pontos')

    return listaCampPilotos

# Formatação da lista de !campConstrutores
def campConstrutoresComando() -> list:

    listaCampConstrutores = []

    qtdConstrutores = keys.qtdConstrutores()
    listaPos = campConstrutores.posicao()
    listaNome = campConstrutores.nome()
    listaPontos = campConstrutores.pontos()
    listaWins = campConstrutores.wins()

    for i in range(qtdConstrutores):
        listaCampConstrutores.append(f'{listaPos[i]} - {listaNome[i]} - {listaPontos[i]} Pontos - {listaWins[i]} Vitórias')

    return listaCampConstrutores

# Formataão da lista de !corrida
def corridaComando() -> list:
    listaCorrida = []

    qtdPilotos = keys.qtdPilotosCorrida()
    listaPosicao = corrida.posicao()
    listaNome = corrida.nome()
    listaSobrenome = corrida.sobrenome()
    listaConstrutores = corrida.construtores()
    listaPontos = corrida.pontos()

    for i in range(qtdPilotos):
        listaCorrida.append(f'{listaPosicao[i]} - {listaNome[i]} {listaSobrenome[i]} - {listaConstrutores[i]} - {listaPontos[i]}')

    return listaCorrida  

# Formatação da lista de !quali
def qualiComando() -> list:
    listaQuali = []

    qtdPilotos = keys.qtdPilotosQuali()
    listaPosicao = corrida.posicao()
    listaNome = quali.nome()
    listaSobrenome = quali.sobrenome()
    listaConstrutores = quali.construtores()
    listaTempo = quali.tempo()

    for i in range(qtdPilotos):
        listaQuali.append(f'{listaPosicao[i]} - {listaNome[i]} {listaSobrenome[i]} - {listaConstrutores[i]} - {listaTempo[i]}')

    return listaQuali

# Formatação da lista de !cosntrutores
def construtoresComando() -> list:
    listaConstrutoresMain = []

    qtdConstrutores = keys.qtdConstrutores()
    listaNome = construtores.nome()
    listaNacionalidade = construtores.nacionalidade()

    for i in range(qtdConstrutores):
        listaConstrutoresMain.append(f'{listaNome[i]} - {listaNacionalidade[i]}')

    return listaConstrutoresMain

# Formatação da lista de !pilotos
def pilotosComando() -> list:
    listaPilotos = []

    qtdPilotos = keys.qtdPilotos()
    listaNumero = pilotos.numero()
    listaCodigo = pilotos.codigo()
    listaNome = pilotos.nome()
    listaFamilia = pilotos.sobrenome()
    listaNacionalidade = pilotos.nacionalidade()

    for i in range(qtdPilotos):
        listaPilotos.append(f'{listaNumero[i]} - {listaCodigo[i]} - {listaNome[i]} {listaFamilia[i]} - {listaNacionalidade[i]}')

    return listaPilotos

# Formatação da lista de !circuitos
def circuitosComando() -> list:
    listaCircuitos = []

    qtdCircuitos = keys.qtdCircuitos()
    listaNome = circuitos.nome()
    listaLocalidade = circuitos.localidade()

    for i in range(qtdCircuitos):
        listaCircuitos.append(f'{listaLocalidade[i]} - {listaNome[i]}')

    return listaCircuitos

# Formatação da lista de !calendario
def calendarioComando() -> list:
    listaCalendario = []
    
    qtdCalendario = keys.qtdCalendario()
    listaQtdCalendario = calendario.qtdCorridas()
    listaGP = calendario.calendarioGP()
    listaData = calendario.datas()

    for i in range(qtdCalendario):
        listaCalendario.append(f'{listaQtdCalendario[i]} - {listaGP[i]} | {listaData[i]}')

    return listaCalendario

if __name__ == "__main__":
    print(qualiComando())