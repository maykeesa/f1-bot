from discord import app_commands
from discord.ext import commands
import sample.formatting as formatting
import discord
import sample.embed as embed

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="$")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!') 
    try:
        synced = await bot.tree.sync()
    except Exception as ex:
        print(ex)

#Log do discord
@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

@bot.tree.command(name="camp-pilotos", description="Mostra o atual campeonato de pilotos")
async def campPilotos(message):
    listaCampPilotosEmbed = formatting.campPilotosComando()
    embedFormatado = embed.campPilotos(message, listaCampPilotosEmbed, bot)
    await message.response.send_message(embed=embedFormatado)

@bot.tree.command(name="camp-construtores", description="Mostra o atual campeonato de construtores")
async def campConstrutores(message):
    listaCampConstrutoresEmbed = formatting.campConstrutoresComando()
    embedFormatado = embed.campConstrutores(message, listaCampConstrutoresEmbed, bot)
    await message.response.send_message(embed=embedFormatado)

@bot.tree.command(name="corrida", description="Mostra o resultado da última corrida")
async def corrida(message):
    listaCorridaEmbed = formatting.corridaComando()
    embedFormatado = embed.corrida(message, listaCorridaEmbed, bot)
    await message.response.send_message(embed=embedFormatado)

@bot.tree.command(name="qualificacao", description="Mostra o resultado da última qualificação")
async def quali(message):
    listaQualiEmbed = formatting.qualiComando()
    embedFormatado = embed.quali(message, listaQualiEmbed, bot)  
    await message.response.send_message(embed=embedFormatado)

@bot.tree.command(name="construtores", description="Mostra todos os construtores da atual temporada")
async def construtores(message):
    listaConstrutores = formatting.construtoresComando()
    embedFormatado = embed.construtores(message, listaConstrutores, bot)
    await message.response.send_message(embed=embedFormatado)
     
@bot.tree.command(name="pilotos", description="Mostra todos os pilotos da atual temporada")
async def pilotos(message):
    listaPilotosEmbed = formatting.pilotosComando()
    embedFormatado = embed.pilotos(message, listaPilotosEmbed, bot)
    await message.response.send_message(embed=embedFormatado)

@bot.tree.command(name="circuitos", description="Mostra todos os circuitos da atual temporada")
async def circuitos(message):
    listaCircuitosEmbed = formatting.circuitosComando()
    embedFormatado = embed.circuitos(message, listaCircuitosEmbed, bot)
    await message.response.send_message(embed=embedFormatado)

@bot.tree.command(name="calendario", description="Mostra o calendârio da atual temporada")
async def calendario(message): 
    listaCalendarioEmbed = formatting.calendarioComando()
    embedFormatado = embed.calendario(message, listaCalendarioEmbed, bot)
    await message.response.send_message(embed=embedFormatado)

bot.run('')
