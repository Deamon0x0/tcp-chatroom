import socket
import threading

host = '127.0.0.1'
port = 1234

nickname = input("Enter your nickname: ")
chat = input("")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break
        
def write(): 
    message = f"{nickname}: {chat}"
    client.send(message.encode('ascii'))
    
rec_thread = threading.Thread(target=receive)
rec_thread.start()

wr_thread = threading.Thread(target=write)
wr_thread.start()