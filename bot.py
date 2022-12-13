# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:48:43 2020

This bot listens for client commands and then inturprets and communicates those commands
to an external socket server hosted my the homeserver.

@Author: John Ulmer
"""

#import os

import discord
import servercheck

#import nest_asyncio
#nest_asyncio.apply()

#the bot needs a token but this is private information. Please provide your own token or ask me about the public one.
token = ''

client = discord.Client()

@client.event
async def on_ready():
    print("{0} has connected to Discord!".format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('hello'):
        await message.channel.send('Fuck you this took forever')

    if message.content.startswith('!status'):
        await message.channel.send(servercheck.getStatus())

    if message.content.startswith('!start'):
        if (servercheck.getStatus() == 'The server is not live!'):
            #function that starts server
            await message.channel.send('Starting Server!')
        else:
            await message.channel.send('The server is either already live or something has gone horribly wrong.')

    if message.content.startswith('!stop'):
        await message.channel.send('The server will shut itself off after 10 minutes of no players.')
        
client.run(token)