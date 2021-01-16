import asyncio
#import websockets
import pickle
import json
import socket
import matplotlib.pyplot as plt

HOST = '192.168.43.163'  # The socket server's hostname or IP address
PORT = 65431        # The port used by the server
Gateway_IP = '192.168.43.163'  # for websocket server

data = ''
connect = 0
loc = ""
ax = []
ay = []
az = []
t = [i for i in range(1,81)]

async def hello(websocket, path):
    while True:
        if connect != 0:
            data = conn.recv(1024).decode('utf-8')
            print('Received from socket server : ', data)
            line = await websocket.recv()
            if line is None:
                return
            await websocket.send(data)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.43.163", 65431))
s.listen()  
conn, addr = s.accept()
f = open("wp.txt", "r")
html = f.readlines()
f.close()
cnt = 0
with conn:
    print('sdsdsd')
    connect = conn
    print(111)
    while True:
        data = conn.recv(1024).decode('utf-8')
        if data[0] != 'x' and data[0] != 'y' and data[0] != 'z':
            continue
        print(data)
        cnt+=1
        fw = open("wp.html", "w")
        if cnt < 5:
            fw.write(html[0][:-1]+ html[1])
            fw.close()
            continue
        gps = conn.recv(1024).decode('utf-8')
        if gps == 'N':
            gps = "25.015215,121.546996"
        fw.write(html[0][:-1] + gps + html[1])
        fw.close()
        
        
        
    	#print('Received from socket server : ', data)
    #start_server = websockets.serve(hello, "192.168.43.163", 8866)

    #asyncio.get_event_loop().run_until_complete(start_server)
    #asyncio.get_event_loop().run_forever()


            


