"""
M2M Lab Exercise 4
Divyam Yadav
Client 1(X and Y in the range 1 to 99) to the Server

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
            X = random.randint(1,100)
            Y = random.randint(1,100)
            data = f"C1:(X,Y)=({X},{Y})"
            send(data)
            time.sleep(2)
    except:
        print("\nServer Has been Terminated")
    finally:
        client.close()