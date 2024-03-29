"""
server.py - Simple Socket Server

"""

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5 

def echo_server(port):
    """ A simple echo server """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print (f'Starting up echo server  on {server_address}')
    sock.bind(server_address)
    # Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog) 
    while True: 
        print ('Waiting to receive message from client')
        client, address = sock.accept() 
        data = client.recv(data_payload) 
        if data:
            print ('Data: {data}')
            client.send(data)
            print ('sent {data} bytes back to {address}')
        # end connection
        client.close() 
   
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple Socket Server')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args() 
    port = given_args.port
    echo_server(port)