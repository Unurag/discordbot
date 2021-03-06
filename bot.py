import discord
from discord.ext import commands
from datetime import datetime
import random
import pymysql
import os
from os import environ

client = commands.Bot(command_prefix='/')
conn = pymysql.connect(user='xxxx', password='xxxx', host='xx',
                       database="botdata")
cur = conn.cursor()


@client.event
async def on_ready():
    print("Bot's ready")
    await client.change_presence(status=discord.Status.do_not_disturb,
                                 activity=discord.Game("Helping Kirmada as always"))


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


@client.command()
async def ping(ms):
    # start = datetime.now()
    # await ms.send("Pong!")
    # end = datetime.now()
    # pi = (end - start).microseconds/1000
    # await ms.send(pi)
    await ms.send(f'You and me are {round(client.latency * 1000)}ms away.')


@client.command()
async def start(ms):
    rnd = random.randint(0, 49)
    cur.execute("SELECT `email` FROM `acc` WHERE id='" + str(rnd) + "'")
    email = cur.fetchone()
    cur.execute("SELECT `pass` FROM `acc` WHERE id='" + str(rnd) + "'")
    pas = cur.fetchone()
    await ms.send(f"**Your latest Netflix account is here**\n\nEmail: **{email[-1]}**\nPassword: **{pas[-1]}**\n\nGenerated by **@Kirmada#3529**")


client.run(environ['TOKEN'])
