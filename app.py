#!/usr/bin/env python3

import socket
from pushbullet import Pushbullet
from datetime import datetime
import os

HOST = ''
PORT = 61337

print("Starting up...")


api_key = os.getenv('PB_API_KEY')
if not api_key:
    print('PB_API_KEY not set')
    exit(1)

pb = Pushbullet(api_key)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Listening on HOST {} PORT {}".format(HOST, PORT))
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                pb.push_note(f"honeypot from {addr[0]}:{addr[1]}", data.decode())
                with open(f"log/{datetime.now().strftime('connection_%Y-%m-%d.log')}", 'a') as f:
                    f.write(f"{addr[0]}:{addr[1]} {data.decode()}\n\n")
                with open('http_response.txt', 'r') as file:
                    conn.sendall(file.read().encode())
        print(f"Connection from {addr} closed")