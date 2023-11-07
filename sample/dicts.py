import requests
from datetime import date

def ano():
    ano = date.today().year
    dataPilotos = requests.get(f'http://ergast.com/api/f1/{ano}/drivers.json')
    pilotosJson = dataPilotos.json()
    qtdPilotos = pilotosJson['MRData']["total"]

    if(qtdPilotos == "0"):
        return date.today().year - 1
    else:
        return date.today().year

anoAtual = ano()

def construtores() -> dict:
    dataConstrutores = requests.get(f'http://ergast.com/api/f1/{anoAtual}/constructors.json')
    return dataConstrutores.json()

def pilotos() -> dict:
    dataPilotos = requests.get(f'http://ergast.com/api/f1/{anoAtual}/drivers.json')
    return dataPilotos.json()

def circuitos() -> dict:
    dataCircuitos = requests.get(f'http://ergast.com/api/f1/{anoAtual}/circuits.json')
    return dataCircuitos.json()

def corrida() -> dict:
    dataCorridas = requests.get(f'http://ergast.com/api/f1/current/last/results.json')
    return dataCorridas.json()

def quali() -> dict:
    ultimaCorrida = corrida()['MRData']["RaceTable"]
    ultimoRound = ultimaCorrida['round']

    dataQuali = requests.get(f'http://ergast.com/api/f1/{anoAtual}/{ultimoRound}/qualifying.json')
    return dataQuali.json()

def calendario() -> dict:
    dataCalendario = requests.get(f'http://ergast.com/api/f1/{anoAtual}.json')
    return dataCalendario.json()

def campPilotos() -> dict:
    dataCampPilotos = requests.get(f'http://ergast.com/api/f1/{anoAtual}/driverStandings.json')
    return dataCampPilotos.json()

def campConstrutores() -> dict:
    dataCampConstrutores = requests.get(f'http://ergast.com/api/f1/{anoAtual}/constructorStandings.json')
    return dataCampConstrutores.json()
