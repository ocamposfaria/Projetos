import discord
from discord.ext import tasks
import pytz
from datetime import datetime
import os
import time
import random
from keep_alive import keep_alive

my_secret = os.environ['discord token']

client = discord.Client()

time.tzset()


def variavel(x):
  global variavel
  variavel = x

camara = 5

#  #  #  #  #  #  #  #  EVENTOS

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('!comandos'):
        await message.channel.send('alguns comandos para você experimentar: \n\n !oi juau robô \n !que vibe \n !me chama de inácio \n !fala pessoal \n !random \n !ativar eventos \n !loteria \n !roleta russa \n\n ou use !patch notes para ver as últimas atualizações')


    if message.content.startswith('!oi juau robô'):
        await message.channel.send('olá otário')


    if message.content.startswith('!que vibe'):
        await message.channel.send('https://www.youtube.com/watch?v=R8gLxW3QFXY')


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
        variavel(message)
        await message.channel.send('você ativou meus eventos para este canal')

    if message.content.startswith('!random'):
      await message.channel.send(str(random.choice(pessoa)) + ' ' + str(random.choice(fato)))

    if message.content.startswith('!loteria'):
      x = random.random()
      if x > 0.0000000199744885:
            await message.channel.send('você não ganhou na loteria')
      else:
            await message.channel.send('PQP VC GANHOU NA LOTERIA NÃO ACREDITO!!!!!!!!!!!!!!!!!!!!!!!!!!!')


    if message.content.startswith('!roleta russa'):

      global camara
      gatilho = random.random()
      prob = 1/(camara + 1)

      if gatilho > prob:
        await message.channel.send(str(message.author.name) + ' não morreu')
        await message.channel.send('agora o revólver só possui {} câmaras livre(s)'.format(camara))
        camara = camara - 1
        
      else:
        await message.channel.send(str(message.author.name) + ' morreu :exploding_head: :gun: ')
        camara = 5


    if message.content.startswith('!patch notes'):
        # await message.channel.send('a versão 1.0 tá no grau: \n - símbolo $ trocado por ! para comandos \n - comando !fala pessoal! alterado para !fala pessoal \n - agora o bot denuncia quem apaga mensagens enviadas \n - retiradas todas as letras maiúsculas em comandos \n - adicionado o comando !random')

        # await message.channel.send('a versão 1.1 tá no grau: \n - adicionado !ativar eventos \n - removido !shrek pois agora ele é um evento \n - adicionado evento \'semana praticamente encerrada\' \n - adicionado status \'ouvindo !comandos\'')

        await message.channel.send('...')

        await message.channel.send('a versão 1.2 tá no grau: \n - agora toda vez que alguém mencionar o nome da prof de produto, o bot responde com \'CUIDADO\' \n - adicionado minigame !roleta russa, que tem 1/6 de chance de te matar \n - adicionado comando !loteria (cada vez que você chama o comando você tem aprox. 1 chance em 50.063.860 de ganhar na loteria (probabilidade da mega-sena) \n - adicionadas mais frases ao comando !random')

        await message.channel.send('a versão 1.2.1 tá no grau: \n - !roleta russa bug fixed')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(type=discord.ActivityType.listening, name="!comandos")
    await client.change_presence(status=discord.Status.online, activity=activity)


@client.event
async def on_message_delete(message):
        await message.channel.send('apagou a mensagem né safado? <@' + str(message.author.id) + '>')


#  #  #  #  #  #  #  #  FATOS RANDOM DATABASE


fato = ['só vacila','fede','é ruim demais no cod','é gente boa','é cringe','quer se formar logo','é comunista','é bolsonarista','abandona os amigos','é maconhista','comeu o cu de quem ta lendo','vai pagar o lanche hoje','ta morrendo de sono','não malhou hoje tsc tsc','se prostituiria pra comer x-burguer','deseja a todos uma boa noite','só queria férias','está cansado de carregar todo mundo nos trabalhos','vai ser o mais rico daqui, convenhamos','perdeu tudo! isso que dá jogar no bicho toda semana','assiste canal de day trader','adora poesia, ele é muito poeteiro','engravidou a namorada, mas ainda não descobriu','compra pack de pézinho escondido','quer ser hardcore mas sua mãe não deixa','quer levar as amizades daqui pra vida toda']

pessoa = ['o arthu','o danieu','o teteu','o juau','o gabireu','o totow']


#  #  #  #  #  #  #  #  LOOP

@tasks.loop(seconds=60)
async def send():

  dia_semana = datetime.now(pytz.timezone('Brazil/East')).weekday()
  hora = datetime.now(pytz.timezone('Brazil/East')).strftime("%H:%M")
  # data = datetime.now(pytz.timezone('Brazil/East')).strftime("%d/%m")
  
  try:

    if dia_semana == 2 and hora == '16:00':
      await variavel.channel.send('são quatro horas da tarde de uma quarta-feira, não é? \n semana praticamente encerrada')

    if dia_semana == 4 and hora == '08:00':
      await variavel.channel.send('https://www.youtube.com/watch?v=8GX9--xhf_A')
      await variavel.channel.send('GRAÇAS A DEUS É SEXTA-FEIRA HEIN @everyone')

    else:
      print('não há eventos no momento (não esqueça de !ativar eventos)')
    
  except:
    print('o evento não aconteceu pois não foi enviado !ativar eventos no canal desejado')

send.start()

#  #  #  #  #  #  #  #  KEEP ALIVE

keep_alive()

client.run(my_secret)
