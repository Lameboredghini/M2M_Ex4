"""
M2M Lab Exercise 4
Divyam Yadav
- Client 3
"""

import socket,time,random,base64

PORT = 10005

SERVER = socket.gethostbyname(socket.gethostname()) 
server_address = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(server_address)


def send(data):
    print(f"Sending {data} to Server")
    message = base64.b64encode(data.encode("utf-8"))
    client.send(message)
    print(client.recv(2048).decode('utf-8')) 


if __name__ == '__main__':
    try:
        while True:
            P = random.randint(100,500)
            Q = random.randint(100,500)
            data = f"C3:(P,Q)=({P},{Q})"
            send(data)
            time.sleep(2)
    except:
        print("\nServer Has been terminated")
    finally:
        client.close()