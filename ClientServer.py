import socket
import select
import sys
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if(len(sys.argv)!=2):
	exit()

user_name_temp = sys.argv[1]

IP_address = "127.0.0.1"
Port = 7000
server.connect(("127.0.0.1", 7000))

init_mssg = socket.gethostbyname(socket.gethostname())

init_other_user = raw_input("To: ")

server.send(init_mssg+"$$"+user_name_temp+"$$"+init_other_user)

 
while True:
 
    
    sockets_list = [sys.stdin, server]
 
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print message
        else:
	    	
            message = sys.stdin.readline()
            server.send(message)
            #sys.stdout.write("YOU SAID:  ")
            #sys.stdout.write(message)
            #sys.stdout.flush()
server.close()
