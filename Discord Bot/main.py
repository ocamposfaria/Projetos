# Author: João Pedro Campos
# Contact: ocamposfaria@gmail.com

# VERSION 1.1.2

#  #  #  #  #  #  #  #  IMPORTING LIBRARIES

import discord
from discord.ext import tasks
import pytz
from datetime import datetime
import os
import time
import random
from keep_alive import keep_alive
import asyncio

#  #  #  #  #  #  #  #  IMPORTING DATA AND SETING UP STUFF

f = open('porta_dos_fundos.txt')  # importing porta_dos_funtos to !porta dos fundos
porta = f.read()
f.close()
porta = eval(porta)

f = open('data_random.txt')  # importing data to !random
fato = f.read()
f.close()
fato = eval(fato)

my_secret = os.environ['discord token']  # set discord token

client = discord.Client()  # set discord client

time.tzset()  # set timezone


def variavel(x):  # set up function to make a global variable
    global variavel
    variavel = x


camara = 4  # set up number of chambers in !roleta russa
nicolas_cage = 0

pessoa = ['o arthu', 'o danieu', 'o teteu', 'o juau', 'o gabireu',
          'o totow']  # SET UP NAMES FOR !random

#  #  #  #  #  #  #  #  CLIENT EVENTS


@client.event
async def on_message(message):
    
    apenas_hora = datetime.now(pytz.timezone('Brazil/East')).strftime("%H")

    if message.content.startswith('!comandos'):
        await message.channel.send(
            'alguns comandos para você experimentar: \n\n !oi juau robô \n !que vibe \n !me chama de inácio \n !fala pessoal \n !random \n !ativar eventos \n !loteria \n !roleta russa \n !adicionar \n !porta dos fundos \n\n ou use !patch notes para ver as últimas atualizações'
        )

    if message.content.startswith('!oi juau robô'):
        await message.channel.send('olá otário')

    if message.content.startswith('!que vibe'):
        await message.channel.send(
            'https://www.youtube.com/watch?v=R8gLxW3QFXY')

    if message.content.startswith('!me chama de inácio'):
        await message.channel.send('Inácio... Inácio?')

    if message.content.startswith('!fala pessoal'):
        await message.channel.send('piroca chegou')

    if 'andrea' in message.content:
        await message.reply('CUIDADO', mention_author=False)
    if 'Andrea' in message.content:
        await message.reply('CUIDADO', mention_author=False)
    if 'andréa' in message.content:
        await message.reply('CUIDADO', mention_author=False)
    if 'Andréa' in message.content:
        await message.reply('CUIDADO', mention_author=False)

    if message.content.startswith('!ativar eventos'):
        try:
            variavel(message)
            #await message.channel.send(
             #   'você ativou meus eventos para este canal')
        except:
            await message.channel.send(
                'você já ativou meus eventos em algum canal')

    if message.content.startswith('!adicionar'):
        global fato
        mensagem = message.content
        fato.append(mensagem[11:])
        f = open('data_random.txt', 'w')
        f.write(str(fato))
        f.close()
        await message.channel.send('novo fato adicionado \'' + mensagem[11:] +
                                   '\'')

    if message.content.startswith('!random'):
        await message.channel.send(
            str(random.choice(pessoa)) + ' ' + str(random.choice(fato)))

    if apenas_hora == '06':
        global nicolas_cage
        if nicolas_cage == 0:
          nicolas_cage = nicolas_cage + 1
          await message.channel.send('https://www.youtube.com/watch?v=m3J0r--l-9w')
          await message.reply('não, e olha o naipezera do moleque essa hora ó, hã he he he, seis hora da manhã e ele todo nicolas cagezinho já hã, turugudum tcha tcha, turugu tcha  turugudum tcha tcha')


    if message.content.startswith('!loteria'):
        x = random.random()
        if x > 0.0000000199:
            await message.channel.send('você não ganhou na loteria')
        else:
            await message.channel.send(
                'PQP VC GANHOU NA LOTERIA NÃO ACREDITO!!!!!!!!!!!!!!!!!!!!!!!!!!!'
            )

    if message.content == '!porta dos fundos':
        await message.channel.send(str(random.choice(porta)))


    if message.content.startswith('!roleta russa'):
        global camara
        gatilho = random.random()
        prob = 1 / (camara + 1)

        if gatilho > prob:
            await message.channel.send(
                str(message.author.name) + ' não morreu')
            await message.channel.send(
                'agora o revólver só possui {} câmaras livre(s)'.format(camara)
            )
            camara = camara - 1

        else:
            await message.channel.send(
                str(message.author.name) + ' morreu :exploding_head: :gun: ')
            camara = 4

    if message.content.startswith('!patch notes'):
        # await message.channel.send('a versão 1.0 tá no grau: \n - símbolo $ trocado por ! para comandos \n - comando !fala pessoal! alterado para !fala pessoal \n - agora o bot denuncia quem apaga mensagens enviadas \n - retiradas todas as letras maiúsculas em comandos \n - adicionado o comando !random')

        # await message.channel.send('a versão 1.1 tá no grau: \n - adicionado !ativar eventos \n - removido !shrek pois agora ele é um evento \n - adicionado evento \'semana praticamente encerrada\' \n - adicionado status \'ouvindo !comandos\'')

        await message.channel.send('...')

        #await message.channel.send('a versão 1.2 tá no grau: \n - agora toda vez que alguém mencionar o nome da prof de produto, o bot responde com \'CUIDADO\' \n - adicionado minigame !roleta russa, que tem 1/6 de chance de te matar \n - adicionado comando !loteria (cada vez que você chama o comando você tem aprox. 1 chance em 50.063.860 de ganhar na loteria (probabilidade da mega-sena) \n - adicionadas mais frases ao comando !random')

        #await message.channel.send('a versão 1.2.1 tá no grau: \n - !roleta russa bug fixed')

        await message.channel.send(
            'a versão 1.2.2 tá no grau: \n - agora o bot não avisa mais quem apagou uma mensagem \n - você pode adicionar fatos ao !random (CUIDADO AO UTILIZAR: INICIE A SENTENÇA COM UM VERBO E DEPOIS COM O RESTANTE DO PREDICADO. exemplo: !adicionar é palestrinha ---> !random ---> juau é palestrinha'
        )

        await message.channel.send(
            '\n a versão 1.3 tá no grau: \n - agora se alguém mandar mensagem entre 6:00 e 6:59 da manhã (incluindo), o bot vai retornar um vídeo e uma frase surpresinha personalizada'
        )
        
        await message.channel.send(
            '\n a versão 1.3.1 tá no grau: \n - adicionado comando !porta dos fundos (retorna um vídeo aleatório do porta dos fundos dentre uma lista dos 50 melhores)'
        )


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(type=discord.ActivityType.listening,
                                name="!comandos")
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)


# @client.event
# async def on_message_delete(message):
#        await message.channel.send('apagou a mensagem né safado? <@' + str(message.author.id) + '>')

#  #  #  #  #  #  #  #  LOOP


@tasks.loop(seconds=60)
async def send():

    dia_semana = datetime.now(pytz.timezone('Brazil/East')).weekday()
    hora = datetime.now(pytz.timezone('Brazil/East')).strftime("%H:%M")
    # data = datetime.now(pytz.timezone('Brazil/East')).strftime("%d/%m")

    try:

        if dia_semana == 2 and hora == '16:00':
            await variavel.channel.send(
                'https://www.youtube.com/watch?v=Tmy5JtL58dE')
            await variavel.channel.send(
                'são quatro horas da tarde de uma quarta-feira, não é?\nsemana praticamente encerrada @everyone')

        if dia_semana == 4 and hora == '08:30':
            await variavel.channel.send(
                'https://www.youtube.com/watch?v=8GX9--xhf_A')
            await variavel.channel.send(
                'GRAÇAS A DEUS É SEXTA-FEIRA HEIN @everyone')
        
        if hora == '00:01':
            nicolas_cage = 0
            print(nicolas_cage)

        else:
            print(str(hora) +'-> não há eventos no momento (não esqueça de !ativar eventos)')

    except:
        print(
            str(hora) +
            '-> o evento não aconteceu pois não foi enviado !ativar eventos no canal desejado'
        )


send.start()

#  #  #  #  #  #  #  #  KEEP ALIVE AND RUN BOT

keep_alive()

client.run(my_secret)