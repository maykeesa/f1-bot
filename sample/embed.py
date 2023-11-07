from datetime import date
import sample.keys as keys
import sample.dicts as dicts
import discord

anoAtual = dicts.ano()
corridaGP = str(keys.corridaNome())

def campPilotos(ctx, listaCampPilotos: list, bot):
    embed = discord.Embed(
        title=f"F1 {anoAtual}: ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":trophy: - Campeonato de Pilotos: ", value="\n".join(listaCampPilotos)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    return embed

def campConstrutores(ctx, listaCampConstrutores: list, bot):
    embed = discord.Embed(
        title=f"F1 {anoAtual} ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":trophy: - Campeonato de Construtores: ", value="\n".join(listaCampConstrutores)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    return embed

def corrida(ctx, listaCorrida: list, bot):
    embed = discord.Embed(
        title=f"{corridaGP} ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":checkered_flag: - Resultado: ", value="\n".join(listaCorrida)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    return embed

def quali(ctx, listaQuali: list, bot):
    embed = discord.Embed(
        title=f"{corridaGP}: ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":checkered_flag: - Qualificação: ", value="\n".join(listaQuali)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    return embed

def construtores(ctx, listaConstrutores: list, bot):
    embed = discord.Embed(
        title=f"F1 {anoAtual} ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":race_car: - Construtores: ", value="\n".join(listaConstrutores)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    return embed
       
def pilotos(ctx, listaPilotos: list, bot):
    embed = discord.Embed(
        title=f"F1 {anoAtual} ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":trophy: - Pilotos: ", value="\n".join(listaPilotos)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    return embed
     
def circuitos(ctx, listaCircuitos: list, bot):
    embed = discord.Embed(
        title=f"F1 {anoAtual} ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":motorway: - Circuitos: ", value="\n".join(listaCircuitos)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    return embed

def calendario(ctx, listaCalendario: list, bot):
    embed = discord.Embed(
        title=f"F1 {anoAtual} ",
        color=0xFF0000,
    )

    embed.set_author(name= bot.user.name, icon_url= bot.user.avatar)
    f1Icon = "https://cdn.discordapp.com/attachments/973660650041638922/977429140414279700/f1logo.png"
    embed.set_thumbnail(url=f1Icon)
    embed.add_field(name=":calendar_spiral: - Calendário: ", value="\n".join(listaCalendario)) 
    embed.set_footer(text="Feito por " + bot.user.name, icon_url= bot.user.avatar)
    return embed
