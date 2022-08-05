from discord.ext import commands
from datetime import date
import discord
import api

anoAtual = date.today().year
bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

#Log do discord
@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

listaCorridaEmbed = []

#!corrida
@bot.command(name="corrida")
async def corrida(message):
    qtdPilotos = len(api.corridaPosicao())
    listaCorridaPosicao = api.corridaPosicao()
    listaCorridaNome = api.corridaNome()
    listaCorridaSobrenome = api.corridaSobrenome()
    listaCorridaPontos = api.corridaPontos()
    listaCorridaConstrutores = api.corridaConstrutores()

    for i in range(qtdPilotos):
        listaCorridaEmbed.append(f'{listaCorridaPosicao[i]} - {listaCorridaNome[i]} {listaCorridaSobrenome[i]} - {listaCorridaConstrutores[i]} - {listaCorridaPontos[i]}')
    await embedCorrida(message)
    listaCorridaEmbed.clear()

#Embed do !corrida
async def embedCorrida(ctx):
    embed = discord.Embed(
        title=f"{api.corridaGP()}: ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar_url)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":checkered_flag: - Resultado: ", value="\n".join(listaCorridaEmbed)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar_url)
    await ctx.send(embed=embed)

listaQualiEmbed = []

#!quali
@bot.command(name="quali")
async def quali(message):
    qtdPilotos = len(api.qualiNome())
    listaQualiPosicao = api.corridaPosicao()
    listaQualiNome = api.qualiNome()
    listaQualiSobrenome = api.qualiSobrenome()
    listaQualiConstrutores = api.qualiConstrutores()
    listaQualiTempo = api.qualiTempo()

    for i in range(qtdPilotos):
        listaQualiEmbed.append(f'{listaQualiPosicao[i]} - {listaQualiNome[i]} {listaQualiSobrenome[i]} - {listaQualiConstrutores[i]} - {listaQualiTempo[i]}')
    await embedQuali(message)
    listaQualiEmbed.clear()

#Embed do !quali
async def embedQuali(ctx):
    embed = discord.Embed(
        title=f"{api.corridaGP()} ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar_url)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":checkered_flag: - Qualificação: ", value="\n".join(listaQualiEmbed)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar_url)
    await ctx.send(embed=embed)
   
listaConstrutoresEmbed = []

#!construtores
@bot.command(name="construtores")
async def construtores(message):
    qtdConstrutores = len(api.construtoresAtual())
    listaConstrutores = api.construtoresAtual()
    listaNacionalidadeConstrutores = api.construtoresNacionalidade()

    for i in range(qtdConstrutores):
        listaConstrutoresEmbed.append(f'{listaConstrutores[i]} - {listaNacionalidadeConstrutores[i]}')
    await embedConstrutores(message)
    listaConstrutores.clear()

#Embed do !construtores
async def embedConstrutores(ctx):
    embed = discord.Embed(
        title=f"F1 {anoAtual} ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar_url)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":race_car: - Construtores: ", value="\n".join(listaConstrutoresEmbed)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar_url)
    await ctx.send(embed=embed)

listaPilotosEmbed = []

#!pilotos        
@bot.command(name="pilotos")
async def pilotos(message):
    qtdPilotos = len(api.pilotosNome())
    listaPilotosNome = api.pilotosNome()
    listaPilotosCode = api.pilotosCodigo()
    listaPilotosNumber = api.pilotosNumero()
    listaPilotosFamily = api.pilotosSobrenome()
    listaPilotosNacionalidade = api.pilotosNacionalidade()

    for i in range(qtdPilotos):
        listaPilotosEmbed.append(f'{listaPilotosNumber[i]} - {listaPilotosCode[i]} - {listaPilotosNome[i]} {listaPilotosFamily[i]} - {listaPilotosNacionalidade[i]}')
    await embedPilotos(message)
    listaPilotosEmbed.clear()

#Embed do !pilotos        
async def embedPilotos(ctx):
    embed = discord.Embed(
        title=f"F1 {anoAtual} ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar_url)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":trophy: - Pilotos: ", value="\n".join(listaPilotosEmbed)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar_url)
    await ctx.send(embed=embed)

listaCircuitosEmbed = []

#!circuitos
@bot.command(name="circuitos")
async def circuitos(message):
    qtdCircuitos = len(api.circuitosAtual())
    listaCircuitosAtual = api.circuitosAtual()
    listaCircuitosLoc = api.circuitosLocalidade()

    for i in range(qtdCircuitos):
        listaCircuitosEmbed.append(f'{listaCircuitosLoc[i]} - {listaCircuitosAtual[i]}')
    await embedCircuito(message)
    listaCircuitosEmbed.clear()

#Embed do !circuitos        
async def embedCircuito(ctx):
    embed = discord.Embed(
        title=f"F1 {anoAtual} ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar_url)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":motorway: - Circuitos: ", value="\n".join(listaCircuitosEmbed)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar_url)
    await ctx.send(embed=embed)

listaCalendarioEmbed = []

#!calendario
@bot.command(name="calendario")
async def calendario(message): 
    qtdCalendario = len(api.circuitosAtual())
    listaQtdCalendario = api.calendarioQtdCorridas()
    listaCalendarioGP = api.calendarioGP()
    listaCalendarioData = api.calendarioData()

    for i in range(qtdCalendario):
        listaCalendarioEmbed.append(f'{listaQtdCalendario[i]} - {listaCalendarioGP[i]} | {listaCalendarioData[i]}')
    await embedCalendario(message)
    listaCalendarioEmbed.clear()

#Embed do !calendario
async def embedCalendario(ctx):
    embed = discord.Embed(
        title=f"F1 {anoAtual} ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar_url)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":calendar_spiral: - Calendário: ", value="\n".join(listaCalendarioEmbed)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar_url)
    await ctx.send(embed=embed)


bot.run('OTczNjU5NzMwMTI1OTE0MTcz.GV49S-._nhq9X77GAO2AQ4WScO9z774TVCawmObZiISCU')