from discord.ext import commands
import discord
import f1api

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

#Log do discord
@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

#!corrida
@bot.command(name="corrida")
async def corrida(message):
    await message.channel.send(f'{message.author.name} a próxima corrida será na Espanha! :flag_es: ')

#!construtores
@bot.command(name="construtores")
async def construtores(message):
    await message.channel.send(f'``` OS CONSTRUTORES DE 2022: ```')
    qtdConstrutores = len(f1api.construtoresAtual())
    for i in range(qtdConstrutores):
        listaConstrutores = f1api.construtoresAtual()
        listaNacionalidadeConstrutores = f1api.nacionalidadeConstrutores()
        await message.channel.send(f'** {listaConstrutores[i]} **  - ** {listaNacionalidadeConstrutores[i]} **')

#!pilotos        
@bot.command(name="pilotos")
async def pilotos(message):
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
@bot.command(name="circuitos")
async def circuitos(message):
    await message.channel.send(f'``` OS CIRCUITOS DE 2022: ```')
    qtdCircuitos = len(f1api.circuitosAtual())
    for i in range(qtdCircuitos):
        listaCircuitosAtual = f1api.circuitosAtual()
        listaCircuitosLoc = f1api.circuitosLocalidade()
        await message.channel.send(f'** {listaCircuitosAtual[i]} ** - ** {listaCircuitosLoc[i]} **')


bot.run('OTczNjU5NzMwMTI1OTE0MTcz.GXy3_C.2vFE73RluCapXDHq6o7YmYgC76Pokk8VOZnxgI')