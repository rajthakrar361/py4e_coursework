# Making a connection to the port, Sending a get request to the port and then getting the data back.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Making a connection to a socket.
mysock.connect(('data.pr4e.org', 80)) # Connecting a socket.
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# CMD was a string in unicode which got converted into bytes.
mysock.send(cmd)

while True:
    # The incoming data was in bytes
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
    # After decoding the data is transformed into UTF-8
mysock.close()
