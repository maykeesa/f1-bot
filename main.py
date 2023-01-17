from discord.ext import commands
import sample.formatting as formatting
import discord
import sample.embed as embed

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="!")


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
    listaCampPilotosEmbed = formatting.campPilotosComando()
    await embed.campPilotos(message, listaCampPilotosEmbed, bot)

#!campConstrutores
@bot.command(name="campConstrutores")
async def campConstrutores(message):
    listaCampConstrutoresEmbed = formatting.campConstrutoresComando() 
    await embed.campConstrutores(message, listaCampConstrutoresEmbed, bot)

#!corrida
@bot.command(name="corrida")
async def corrida(message):
    listaCorridaEmbed = formatting.corridaComando()
    await embed.corrida(message, listaCorridaEmbed, bot)

#!quali
@bot.command(name="quali")
async def quali(message):
    listaQualiEmbed = formatting.qualiComando()  
    await embed.quali(message, listaQualiEmbed, bot)

#!construtores
@bot.command(name="construtores")
async def construtores(message):
    listaConstrutores = formatting.construtoresComando()
    await embed.construtores(message, listaConstrutores, bot)

#!pilotos        
@bot.command(name="pilotos")
async def pilotos(message):
    listaPilotosEmbed = formatting.pilotosComando()
    await embed.pilotos(message, listaPilotosEmbed, bot)

#!circuitos
@bot.command(name="circuitos")
async def circuitos(message):
    listaCircuitosEmbed = formatting.circuitosComando()
    await embed.circuito(message, listaCircuitosEmbed, bot)

#!calendario
@bot.command(name="calendario")
async def calendario(message): 
    listaCalendarioEmbed = formatting.calendarioComando()
    await embed.calendario(message, listaCalendarioEmbed, bot)

bot.run('OTczNjU5NzMwMTI1OTE0MTcz.GctLIx.3ackILrKVtSZfOYjEiFb8C9YhyKOsyqCmn_A1Q')
