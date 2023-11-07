import sample.dicts as dicts

#Datas das API's de Contrutores, Pilotos, Circuitos e Resultados
construtoresJson = dicts.construtores()
pilotosJson = dicts.pilotos()
circuitosJson = dicts.circuitos()
corridaJson = dicts.corrida()
qualiJson = dicts.quali()
calendarioJson = dicts.calendario()
campeonatoPiJson = dicts.campPilotos()
campeonatoCoJson = dicts.campConstrutores()

# Keys Principais
def construtores() -> dict:
    construtoresTabela = construtoresJson['MRData']["ConstructorTable"]
    return construtoresTabela['Constructors']

def pilotos() -> dict:
    pilotosTabela = pilotosJson['MRData']["DriverTable"]
    return pilotosTabela['Drivers']

def circuitos() -> dict:
    circuitosTabela = circuitosJson['MRData']["CircuitTable"]
    return circuitosTabela['Circuits']

def corrida() -> dict:
    corridaTabela = corridaJson['MRData']["RaceTable"]
    return corridaTabela['Races']

def corridaResultado() -> dict:
    corridaTabela = corridaJson['MRData']["RaceTable"]
    corrida = corridaTabela['Races']
    return corrida[0]['Results']

def corridaNome() -> dict:
    corridaTabela = corridaJson['MRData']["RaceTable"]
    races = corridaTabela['Races'][0]
    return races["raceName"]

def quali() -> dict:
    qualiTabela = qualiJson['MRData']["RaceTable"]
    quali = qualiTabela['Races']
    return quali[0]['QualifyingResults']

def calendario() -> dict:
    calendarioTabela = calendarioJson['MRData']["RaceTable"]
    return calendarioTabela['Races']

def campConstrutores() -> dict:
    campConsTabela = campeonatoCoJson['MRData']["StandingsTable"]
    campConsLista = campConsTabela['StandingsLists']
    return campConsLista[0]['ConstructorStandings']

def campPilotos() -> dict:
    campPilotoTabela = campeonatoPiJson['MRData']["StandingsTable"]
    campPilotoLista = campPilotoTabela['StandingsLists']
    return campPilotoLista[0]['DriverStandings']

# Key Qtd

def qtdPilotos() -> int:
    return int(pilotosJson['MRData']["total"])

def qtdConstrutores() -> int:
    return int(construtoresJson['MRData']["total"])

def qtdCircuitos() -> int:
    return int(circuitosJson['MRData']["total"])

def qtdPilotosCorrida() -> int:
    return int(corridaJson['MRData']["total"])

def qtdPilotosQuali() -> int:
    return int(qualiJson['MRData']["total"])

def qtdCalendario() -> int:
    return int(calendarioJson['MRData']["total"])

if __name__ == '__main__':
    print(corrida())