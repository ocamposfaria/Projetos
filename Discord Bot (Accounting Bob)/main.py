import discord
import os
import datetime
import discord.ext
#from discord.utils import get
from discord.ext import commands  #, tasks
#from discord.ext.commands import has_permissions, CheckFailure, check
#from keep_alive import keep_alive
import pandas as pd
import pytz
import sqlalchemy as sqla

# SETTING UP
client = discord.Client()

# CLIENT PREFIX
client = commands.Bot(command_prefix='!')

############################################# START BOT FUNCTIONS


@client.event
async def on_ready():
    print('sponge bob is ready to note spends')


@client.command()
async def commands(ctx):
    await ctx.send(
        'type "!credit {value} {name} {category}"\nfor registers on credit\n\nor\n\ntype "!debit {value} {name} {category}"\nfor registers on debit\n\n*attention: {category} must not have spaces!'
    )


@client.command()
async def credit(ctx):
    # getting value, name and category of spend
    split = ctx.message.content.split()
    name = []
    for i in range(len(split)):
        if i == 1:
            value = split[1]
        if i < len(split) - 1 and i > 1:
            name = name + [split[i]]
        if i == len(split) - 1:
            category = split[i]
        else:
            pass
    name = ' '.join(name)

    # passing timestamp, name, category, value to table

    try:
        df = pd.read_csv(str(ctx.message.author))
        row = pd.Series(
            [
                datetime.datetime.now(
                    pytz.timezone('Etc/GMT+3')).strftime("%d/%m/%Y"),
                name, category, value, 'credit'
            ],
            index=['updated_at', 'name', 'category', 'value', 'type'])
        df = df.append([row], ignore_index=True)
        df.to_csv(str(ctx.message.author), index=False)

    except Exception as e:
        print(e)
        try:
            df = pd.DataFrame(
                columns=['updated_at', 'name', 'category', 'value', 'type'])
            df.to_csv(str(ctx.message.author), index=False)
            await ctx.send(
                'This is your first input, so I created a new list of spends for you.'
            )

            df = pd.read_csv(str(ctx.message.author))
            row = pd.Series([
                datetime.datetime.now(
                    pytz.timezone('Etc/GMT+3')).strftime("%d/%m/%Y"),
                name, category, value, 'credit'
            ],
                            index=[
                                'updated_at', 'name', 'category', 'value',
                                'type'
                            ])
            df = df.append([row], ignore_index=True)
            df.to_csv(str(ctx.message.author), index=False)

        except Exception as e:
            await ctx.send(f'ERROR: {str(e)}')

# sending message
    embed = discord.Embed(title=f'R$ {value} → {name}',
                          description=f'{category}, on credit',
                          color=discord.Color.blue())
    await ctx.send('Let me register this for you.')
    await ctx.send(embed=embed)


@client.command()
async def debit(ctx):
    # getting value, name and category of spend
    split = ctx.message.content.split()
    name = []
    for i in range(len(split)):
        if i == 1:
            value = split[1]
        if i < len(split) - 1 and i > 1:
            name = name + [split[i]]
        if i == len(split) - 1:
            category = split[i]
        else:
            pass
    name = ' '.join(name)

    # passing timestamp, name, category, value to table

    try:
        df = pd.read_csv(str(ctx.message.author))
        row = pd.Series(
            [
                datetime.datetime.now(
                    pytz.timezone('Etc/GMT+3')).strftime("%d/%m/%Y"),
                name, category, value, 'debit'
            ],
            index=['updated_at', 'name', 'category', 'value', 'type'])
        df = df.append([row], ignore_index=True)
        df.to_csv(str(ctx.message.author), index=False)

    except Exception as e:
        print(e)
        try:
            df = pd.DataFrame(
                columns=['updated_at', 'name', 'category', 'value', 'type'])
            df.to_csv(str(ctx.message.author), index=False)
            await ctx.send(
                'This is your first input, so I created a new list of spends for you.'
            )

            df = pd.read_csv(str(ctx.message.author))
            row = pd.Series([
                datetime.datetime.now(
                    pytz.timezone('Etc/GMT+3')).strftime("%d/%m/%Y"),
                name, category, value, 'debit'
            ],
                            index=[
                                'updated_at', 'name', 'category', 'value',
                                'type'
                            ])
            df = df.append([row], ignore_index=True)
            df.to_csv(str(ctx.message.author), index=False)

        except Exception as e:
            await ctx.send(f'ERROR: {str(e)}')

    # sending message
    embed = discord.Embed(title=f'R$ {value} → {name}',
                          description=f'{category}, on debit',
                          color=discord.Color.blue())
    await ctx.send('Let me register this for you.')
    await ctx.send(embed=embed)
	


@client.command()
async def sendtosql(ctx):
	df = pd.read_csv('ocamposfaria#3938', sep=',',decimal=',')
	# df['value'] = df['value'].replace(',','.')
	df['value'] = df['value'].astype('float64')
	engine = sqla.create_engine("mysql+pymysql://" + "admin" + ":" + "oldnumber7" + "@" + "accountingbob.cs8refzom5ab.us-east-1.rds.amazonaws.com" + "/" + "bob")
	df.to_sql(str(ctx.message.author), con = engine, if_exists = 'replace',index = False, chunksize = None)
	await ctx.send("Sending data to AWS's database")

	
############################################# END BOT FUNCTIONS

# RUN BOT
client.run('')
