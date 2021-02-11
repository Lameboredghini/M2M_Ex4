"""
M2M Lab Exercise 4
Divyam Yadav
- Server
"""
import socket, threading, base64

PORT = 10005
SERVER = socket.gethostbyname(socket.gethostname()) 
server_address = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(server_address)


def handle_client(connection,address):
    print(f"New Client with Address {address} Connected.")
    while True:
        message = connection.recv(2048)
        if not message:
            break
        decoded_bytes = base64.b64decode(message)
        data = str(decoded_bytes,"utf-8")
        print(f"From Address:{address}, Message:{data}")
        connection.send(f"Received {data[3:]}!".encode('utf-8'))
    
    print(f"Client {address} is Disconnected!")
    connection.close() 


def run_server():
    server.listen()
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client,args=(connection,address)) 
        thread.start()
        print(f"Number of Active Clients: {threading.activeCount()-1}")

if __name__ == '__main__':
    try:
        print("Server has been started")
        run_server()
    except:
        print("\nTerminating server")
    finally:
        server.close()
