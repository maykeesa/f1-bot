from discord.ext import commands
import formatting
import embed

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

#Log do discord
@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

#!campPilotos
@bot.command(name="campPilotos")
async def campPilotos(message):
    listaCampPilotosEmbed = formatting.campPilotos()
    await embed.campPilotos(message, listaCampPilotosEmbed, bot)

#!campConstrutores
@bot.command(name="campConstrutores")
async def campConstrutores(message):
    listaCampConstrutoresEmbed = formatting.campConstrutores() 
    await embed.campConstrutores(message, listaCampConstrutoresEmbed, bot)

#!corrida
@bot.command(name="corrida")
async def corrida(message):
    listaCorridaEmbed = formatting.corrida()
    await embed.corrida(message, listaCorridaEmbed, bot)

#!quali
@bot.command(name="quali")
async def quali(message):
    listaQualiEmbed = formatting.quali()  
    await embed.quali(message, listaQualiEmbed, bot)

#!construtores
@bot.command(name="construtores")
async def construtores(message):
    listaConstrutores = formatting.construtores()
    await embed.construtores(message, listaConstrutores, bot)

#!pilotos        
@bot.command(name="pilotos")
async def pilotos(message):
    listaPilotosEmbed = formatting.pilotos()
    await embed.pilotos(message, listaPilotosEmbed, bot)

#!circuitos
@bot.command(name="circuitos")
async def circuitos(message):
    listaCircuitosEmbed = formatting.circuitos()
    await embed.circuito(message, listaCircuitosEmbed, bot)

#!calendario
@bot.command(name="calendario")
async def calendario(message): 
    listaCalendarioEmbed = formatting.calendario()
    await embed.calendario(message, listaCalendarioEmbed, bot)

bot.run('OTczNjU5NzMwMTI1OTE0MTcz.GOPoHI.0GRQ1sQX1z9_sf_CM48L2eysUUANZzkcL934E4')