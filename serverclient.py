# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21

Client end of the socket server to the integrated with the discordbot.
No longer Needed
@Author: John Ulmer
"""

import socket

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    while True:
        text = input()
        if text == "quit":
            break
        s.send(bytes(text, "UTF-8"))