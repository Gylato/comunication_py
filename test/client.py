import socket
import threading

# Elegir nickname
nickname = input("Choose your nickname: ")

# Conectar al servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.X', 55555))  # Reemplaza X con la última parte de la IP del servidor

# Escuchar al servidor y enviar nickname
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

# Enviar mensajes al servidor
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

# Iniciar hilos para escuchar y escribir
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
