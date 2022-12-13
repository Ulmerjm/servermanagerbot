# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:48:43 2020

Uses the Minecraft Server library to check the server staus and return a result based on user provide args.

@Author: John Ulmer
"""

from mcstatus import MinecraftServer

# the below constructor takes an ip and port argument, again this is not public and needs to be provided.
server = MinecraftServer()

def getStatus(opt = 0):
    
    try:
        status = server.status()
        if opt == 0 :
            return('The server has {0} players.'.format(status.players.online))
        else:
            return('The server has {0} players and replied in {1} ms'.format(status.players.online, status.latency))
    except(ConnectionRefusedError):
        return('The server is not live!')
