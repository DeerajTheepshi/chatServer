import socket
import select
import sys
from thread import *
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
server.bind(("127.0.0.1", 7000))

server.listen(3)
 
clientMap = {}
groupMap = {}


userIP = ""
userName = ""
userTarget = ""
 
def clientthread(conn, addr):
 

    conn.send("Diprivi Welcomes you!")

    init_list = init_mssg.split("$$")
    userIP = init_list[0]
    userName = init_list[1]
    userTarget = init_list[2]
    clientMap[userName] = conn
 
    while True:
            try:
                message = conn.recv(2048)
                if message:
 
                    print addr[0] + "> " + message
 
                    message_to_send =  addr[0] + ">> " + message

                    kaala(message_to_send, conn,userTarget)
 
                else:
                    remove(conn,userTarget)
 
            except:
                continue
 
def kaala(message, connection,target):
    client = clientMap[target]
    try:
       	client.send(message)
    except:
        client.close()
 
        remove(clients,target)
 
def remove(connection,target):
    if connection in list_of_clients:
        del clientMap[target]
 
while True:
 
    conn, addr = server.accept()
 
    print addr[0] + " connected"

    init_mssg = conn.recv(1024)
 
    start_new_thread(clientthread,(conn,addr))    
 
conn.close()
server.close()
