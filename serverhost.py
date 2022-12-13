# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21

Establishes the socket server which listens for input from discord.
No Longer Needed
@Author: John Ulmer
"""

import socket

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)

            if data:
                message = data.decode("utf-8")
                print(message)