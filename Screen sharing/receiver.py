from vidstream import StreamingServer
import threading

receiver=StreamingServer('192.168.0.17',9999)

t=threading.Thread(target=receiver.start_stream())
t.start()

while input("") != 'STOP':
  continue

receiver.start_server()
