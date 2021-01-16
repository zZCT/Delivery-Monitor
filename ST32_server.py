import asyncio
import websockets
import pickle
import json
import socket
import matplotlib.pyplot as plt

HOST = '192.168.43.163'  # The socket server's hostname or IP address
PORT = 65431        # The port used by the server
Gateway_IP = '192.168.43.163'  # for websocket server

data = ''
connect = 0

async def ws(websocket, path):
    loc = ""
    ax = []
    ay = []
    az = []
    t = [i for i in range(1,81)]
    while True:
        data = conn.recv(1024).decode('utf-8')
        print(data)
        if data[0] != 'x' or data[0] != 'y' or data[0] != 'z':
            continue
        data = conn.recv(1024).decode('utf-8')
        print(data)
        '''
        c=0
        while c < 80:
            data = conn.recv(1024).decode('utf-8').split(",")
            print(data)
            if data[0] == "":
                continue
            ax.append(float(data[0]))
            ay.append(float(data[1]))
            az.append(float(data[2]))
            c += 1
        plt.plot(t, ax, color=(255/255,100/255,100/255))
        plt.plot(t, ay, color=(100/255,255/255,100/255))
        plt.plot(t, az, color=(100/255,100/255,255/255))
        plt.title("acceleration")
        plt.savefig('acc.png')
        plt.show()
        ax = []
        ay = []
        az = []
        f = open('acc.png')
        if loc == "":
            loc = "25.017860,121.544065"
            '''
        f = open('mywebpage.txt')
        html = f.readlines()
        response = html[0] + loc + html[1]
        conn.send(response.encode())
        f.close()
        loc = ""
        await websocket.send(data)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.43.163", 65431))
s.listen()  
conn, addr = s.accept()
with conn:
    print('sdsdsd')
    connect = conn
    start_server = websockets.serve(ws, Gateway_IP, 8866)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    



            


