import discord
import f1api

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        #Log do discord
        print(f'Message from {message.author}: {message.content}')

        # !corrida
        if message.content == '!corrida':
            await message.channel.send(f'{message.author.name} a próxima corrida será na Espanha! :flag_es: ')

        # !construtores
        elif message.content == '!construtores':
            await message.channel.send(f'``` OS CONSTRUTORES DE 2022: ```')
            qtdConstrutores = len(f1api.construtoresAtual())
            for i in range(qtdConstrutores):
                listaConstrutores = f1api.construtoresAtual()
                listaNacionalidadeConstrutores = f1api.nacionalidadeConstrutores()
                await message.channel.send(f'** {listaConstrutores[i]} **  - ** {listaNacionalidadeConstrutores[i]} **')
        
        # !pilotos
        elif message.content == '!pilotos':
            await message.channel.send(f'``` OS PILOTOS DE 2022: ```')
            qtdPilotos = len(f1api.pilotosName())
            for i in range(qtdPilotos):
                listaPilotosNome = f1api.pilotosName()
                listaPilotosCode = f1api.pilotosCode()
                listaPilotosNumber = f1api.pilotosNumber()
                listaPilotosFamily = f1api.pilotosFamilyName()
                listaPilotosNacionalidade = f1api.pilotosNacionalidade()
                await message.channel.send(f'** {listaPilotosNumber[i]} ** - ** {listaPilotosCode[i]} ** - ** {listaPilotosNome[i]} {listaPilotosFamily[i]} ** - ** {listaPilotosNacionalidade[i]} **')
        
        # !circuitos
        elif message.content == '!circuitos':
            await message.channel.send(f'``` OS CIRCUITOS DE 2022: ```')
            qtdCircuitos = len(f1api.circuitosAtual())
            for i in range(qtdCircuitos):
                listaCircuitosAtual = f1api.circuitosAtual()
                listaCircuitosLoc = f1api.circuitosLocalidade()
                await message.channel.send(f'** {listaCircuitosAtual[i]} ** - ** {listaCircuitosLoc[i]} **')

client = MyClient()
client.run('')
