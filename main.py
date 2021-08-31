import discord,  time
from discord.ext import commands
import random
import minigames
from datetime import datetime
from discord import Embed

client = commands.Bot(command_prefix='a!')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('anbu!ajuda'))
    print('### ANBU IS ONLINE ###')

@client.command(name='ajuda')
async def ajuda(ctx):
    embed = discord.Embed(title='Meus Comandos:', colour=discord.Colour.dark_grey())
    embed.add_field(name='**a!creditos**', value='Pra vc me conhecer melhor...')
    embed.add_field(name='**a!ajuda**', value='Pra vc me conhecer melhor...')
    embed.add_field(name='**a!membros**', value='mostro a quantidade de membros no servidor')
    embed.add_field(name='**a!pergunta **', value='respondo qualquer pergunta que vc fizer depois do comando')
    embed.add_field(name='**a!gostosura **', value='mostro o seu nível de gostosura')
    embed.add_field(name='**a!casal **', value='mostro a porcentagem de formar um belo casal')
    embed.add_field(name='**a!playcc**', value='Jogar Cara ou Coroa')

    await ctx.send(embed=embed)


@client.command(name='creditos')
async def creditos(ctx):
    await ctx.send(f'''**CRÉDITOS:**           
                YouTube: https://www.youtube.com/channel/UCiwijb7fnTlw6j4EAM9HihQ/featured
                Twitter: https://twitter.com/F4_exe
                Twitch:  https://www.twitch.tv/f4_zzz
                ''')


@client.command(name='pergunta')
async def pergunta(ctx):
    respostas = ['Sim', 'Não', 'talvez', 'Com ctz não', 'Com ctz', 'Óbvio', 'Se vira ae, vou responder não']
    await ctx.send(random.choice(respostas))

@client.command(name='gostosura')
async def gostosura(ctx):
    percent = random.randint(0, 100)
    embed = discord.Embed(title="Seu nível de gostosura é ", colour=discord.Colour.dark_grey())
    embed.add_field(name='...........................', value=f'###  **{percent}%**  ###')
    await ctx.send(embed=embed)

@client.command(name='casal')
async def casal (ctx):
    percent = random.randint(0, 100)
    embed = discord.Embed(title='A porcentagem de vcs formarem um belo casal é...', colour=discord.Colour.dark_grey())
    embed.add_field(name='...........................', value=f'###  **{percent}%**  ###')
    await ctx.send(embed=embed)

@client.command(name='playcc')
async def playcc (ctx):
    minigames.cc()
    await ctx.send('---------')
    await ctx.send('--- 3 ---')
    time.sleep(0.5)
    await ctx.send('--- 2 ---')
    time.sleep(0.5)
    await ctx.send('--- 1 ---')
    time.sleep(0.5)
    await ctx.send(f'-**{minigames.cc()}**-')
    await ctx.send('---------')


@client.command(name='membros')
async def membros (ctx):
    id = client.get_guild({guild})
    embed = discord.Embed(title='Número De Membros:', colour=discord.Colour.dark_grey())
    embed.add_field(name='.......................', value=f'Atualmente, o servidor possui **{id.member_count}**  membros')
    await ctx.send(embed=embed)


client.run('Bot Token')
