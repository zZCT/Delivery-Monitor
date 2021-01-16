import socket 
import time
import sys # In order to terminate the program
import os

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Prepare a sever socket
# TODO start
host, port = '127.0.0.1' , 12346
serverSocket.bind((host, port))
# TODO in end
while True:
    #Establish the connection
    print('Ready to serve...')
    # TODO start
    serverSocket.listen(5)
    c, address = serverSocket.accept()
    # TODO end
    try:
        # Receive http request from the clinet
        # TODO start

        message = c.recv(1024).decode()
        # TODO end
        print(message)

        filename = message.split()[1]
        print(filename)
        f = open(filename[1:],"r")
        
        # Read data from the file that the client requested
        # Split the data into lines for future transmission 
        # TODO start
        outputdata = f.readline()
        f.close()
        #header = r
        # TODO end
        print(outputdata)

        #Send one HTTP header line into socket
        # TODO start
        #serverSocket.send(header.encode())
        # send HTTP status to client
        c.send('HTTP/1.1 200 OK\r\n'.encode())
        # send content type to client
        if(filename.endswith(".jpg")):
            filetype = 'image/jpg'
        elif(filename.endswith(".css")):
            filetype = 'text/css'
        else:
            filetype = 'text/html'
        # TODO end
        c.send('Content-Type: '.encode()+str(filetype).encode()+'\n\n'.encode())
        # TODO end
        # Send the content of the requested file to the client  
        for i in range(0, len(outputdata)):
            c.send(outputdata[i].encode())
        c.send("\r\n".encode())

        c.close()
    except IOError:
        #Send response message for file not found
        # TODO start
        header = 'HTTP/1.1 404 Not Found\r\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'
        #c.send(header.encode())
        c.send(response.encode())
        # TODO end

        #Close client socket
        # TODO start
        c.close()
        # TODO end
serverSocket.close()
sys.exit()
