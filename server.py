import socket
import threading

host = "127.0.0.1"
port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

## broadcast message 

def broadcast(message):
    for client in clients:
        client.send(message.encode('ascii'))
        
## Handle individual clients  
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)   
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat".encode('ascii'))
            nicknames.remove(nickname)
            break

# receive message and setup nickname

def receive():
    while True:
        client, address = server.accept()
        print(f"connect with {str(address)}")
        
        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f"nickname of client is {nickname}")
        broadcast(f"Welcome {nickname} to DeamonServer")
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
print(f"[*] Server is listening on {host, port} [*]")

receive()       
   
   
        
# import socket
# import threading

# host = '127.0.0.1'
# port = 7777

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((host, port))
# server.listen()

# clients = []
# nicknames = []

# def broadcast(message):
#     for client in clients:
#         client.send(message.encode('ascii'))
        
# def handle(client):
#     while True:
#         try:
#             message = client.recv(1024)
#             broadcast(message)
#         except:
#             index = clients.index(client)
#             clients.remove(client)
#             client.close()
#             nickname = nicknames[index]
#             broadast(f"{nickname} left!".encode('ascii'))
#             nicknames.remove(nickname)
#             break
        
# def receive():
#     while True:
#         client, address = server.accept()
#         print(f"connected with {str(address)}")
#         client.send('code'.encode('ascii'))
#         nickname = client.recv(1024).decode('ascii')
#         nicknames.append(nickname)
#         clients.append(client)
#         print(f"nickname of client is {nickname}")
#         broadcast(f"welcome to deamon server {nickname}")
#         thread = threading.Thread(target=handle, args=(client, ))
#         thread.start()
        
# receive()
