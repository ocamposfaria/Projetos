import discord
import os
import datetime
import discord.ext
#from discord.utils import get
from discord.ext import commands  #, tasks
#from discord.ext.commands import has_permissions, CheckFailure, check
from keep_alive import keep_alive
import pandas as pd
import pytz

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
        '!spent [value] [name] [category]\n*category input must not have spaces'
    )

@client.command()
async def spent(ctx):
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
        row = pd.Series([
            datetime.datetime.now(
                pytz.timezone('Etc/GMT+3')).strftime("%d/%m/%Y %H:%M:%S"),
            name, category, value
        ],
                        index=['updated_at', 'name', 'category', 'value'])
        df = df.append([row], ignore_index=True)
        df.to_csv(str(ctx.message.author), index=False)

    except Exception as e:
        print(e)
        try:
            df = pd.DataFrame(
                columns=['updated_at', 'name', 'category', 'value'])
            df.to_csv(str(ctx.message.author), index=False)
            await ctx.send(
                'This is your first input, so I created a new list of spends for you.'
            )

            df = pd.read_csv(str(ctx.message.author))
            row = pd.Series([
                datetime.datetime.now(
                    pytz.timezone('Etc/GMT+3')).strftime("%d/%m/%Y %H:%M:%S"),
                name, category, value
            ],
                            index=['updated_at', 'name', 'category', 'value'])
            df = df.append([row], ignore_index=True)
            df.to_csv(str(ctx.message.author), index=False)

        except Exception as e:
            await ctx.send(str(e))

    # sending message
    embed = discord.Embed(title=f'R$ {value} → {name}',
                          description=f'{category}',
                          color=discord.Color.blue())
    await ctx.send('Let me register this for you.')
    await ctx.send(embed=embed)


############################################# END BOT FUNCTIONS

# RUN KEEP ALIVE
keep_alive()

# RUN BOT
client.run(os.getenv('TOKEN'))
