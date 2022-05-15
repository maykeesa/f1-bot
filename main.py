import discord
from discord.ext import commands
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
            l = 0
            await message.channel.send(f'``` OS CONSTRUTORES DE 2022: ```')
            for i in f1api.construtoresAtual():
                for j in range(1):
                    listaNacionalidadeConstrutores = f1api.nacionalidadeConstrutores()
                    await message.channel.send(f'** {i} **  - *** {listaNacionalidadeConstrutores[l]} ***')
                    l += 1
                    break
        
        # !pilotos
        elif message.content == '!pilotos':
            l = 0
            await message.channel.send(f'``` OS PILOTOS DE 2022: ```\n')
            for i in f1api.pilotosName():
                for j in range(1):
                    listaPilotosCode = f1api.pilotosCode()
                    listaPilotosNumber = f1api.pilotosNumber()
                    listaPilotosFamily = f1api.pilotosFamilyName()
                    listaPilotosNacionalidade = f1api.pilotosNacionalidade()
                    await message.channel.send(f'** {listaPilotosNumber[l]} ** - ** {listaPilotosCode[l]} ** - ** {i} {listaPilotosFamily[l]} ** - ** {listaPilotosNacionalidade[l]} **')
                    l += 1
                    break

client = MyClient()
client.run('OTczNjU5NzMwMTI1OTE0MTcz.GXy3_C.2vFE73RluCapXDHq6o7YmYgC76Pokk8VOZnxgI')