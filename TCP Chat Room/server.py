import threading
import socket

host='127.0.0.1' #localhost
port=55555

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients=[]
nicknames=[]

def broadcast(message):
  for client in clients:
    client.send(message)

def handle(client):
  while True:
    try:
      msg = message = client.recv(1024)
      if msg.decode('ascii').startswith('KICK'):
        if nicknames[clients.index(client)] == 'admin':
          name_to_kick=msg.decode('ascii')[5:]
          kick_user(name_to_kick)
        else:
          clients.send('Command was refused!'.encode('ascii'))
      elif msg.decode('ascii').startswith('BAN'):
        if nicknames[clients.index(client)] == 'admin':
          name_to_ban=msg.decode('ascii')[4:]
          kick_user(name_to_ban)
          with open('bans.txt','a') as f:
            f.write(f'{name_to_ban}\n')
          print(f'{name_to_ban} was banned!')
        else:
          clients.send('Command was refused!'.encode('ascii'))        
        
      else:
        broadcast(message)
    except:
      if client in clients:
        index=clients.index(client)
        clients.remove(client)
        nickname=nicknames[index]
        broadcast(f'{nickname} left the chat'.encode('ascii'))
        nicknames.remove(nickname)
        break

def receive():
  while True:
    client,address=server.accept()
    print(f"Connected with {str(address)}")
    client.send('NICK'.encode('ascii'))
    nickname=client.recv(1024).decode('ascii')
    with open('bans.txt','r') as f:
      bans=f.readlines()
    if nickname+'\n' in bans:
      client.send('BAN'.encode('ascii'))
      client.close()
      continue
    if nickname == 'admin':
      client.send('PASS'.encode('ascii'))
      password=client.recv(1024).decode('ascii')
      if password != 'adminpass':
        client.send('REFUSE'.encode('ascii'))
        client.close()
        continue
    nicknames.append(nickname)
    clients.append(client)
    print(f'Nickname of the client is {nickname}!')
    broadcast(f'{nickname} joined the chat!'.encode('ascii'))
    client.send('Connected to the server!'.encode('ascii'))
    thread=threading.Thread(target=handle,args=(client,))
    thread.start()

def kick_user(name):
  if name in nicknames:
    name_index = nicknames.index(name)
    client_to_kick = clients[name_index]
    clients.remove(client_to_kick)
    client_to_kick.send('You were kicked by admin!'.encode('ascii'))
    client_to_kick.close()
    nicknames.remove(name)
    broadcast(f'{name} was kicked by an admin!'.encode('ascii'))

print("Server is listening....")
receive()
