"""
M2M Lab Exercise 4
- Client that sends the TCP requests 
( A and B in the range 500 to 999) to the Server
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
            A = random.randint(50,1000)
            B = random.randint(50,1000)
            data = f"C2:(A,B)=({A},{B})"
            send(data)
            time.sleep(2)
    except:
        print("\nServer has been Terminated")
    finally:
        client.close()