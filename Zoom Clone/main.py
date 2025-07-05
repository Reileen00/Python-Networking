from vidtream import *
import tkinter as tk
import socket 
import threading
import requests

public_ip_address=requests.get('https://api.ipify.org')
local_ip_address=socket.gethostbyname(socket.gethostname())
server=StreamingServer('192.168.0.207',9999)
print(local_ip_address)
receiver=AudioReceiver(local_ip_address,8888)

def start_listening():
  t1=threading.Thread(target=server.start_server) 
  t2=threading.Thread(target=receiver.start_server)
  t1.start()
  t2.start()

def start_camera_stream():
  camera_client=CameraClient(text_target_ip.get(1.0,'end-1c'),7777)
  t3=threading.Thread(target=camera_client.start_stream)
  t3.start()

def start_screen_sharing():
  screen_client=ScreenSharingClient(text_target_ip.get(1.0,'end-1c'),7777)
  t4=threading.Thread(target=screen_client.start_stream)
  t4.start()

def start_audio_stream():
  audio_sender=AudioSender(text_target_ip.get(1.0,'end-1c'),6666)
  t5=threading.Thread(target=audio_sender.start_stream)
  t5.start()

#GUI
window=tk.Tk()
window.title("NeuralNine Calls v0.0.1 Alpha")
window.geometry('300x200')
label_target_ip = tk.label(window,text="Target IP:")
label_target_ip.pack()

text_target_ip=tk.Text(window,height=1)
text_traget_ip.pack()

btn_listen=tk.Button(window,text="Start Listening",width=50,command=start_listening)
btn_listen.pack(anchor=tk.CENTER,expand=True)

btn_camera=tk.Button(window,text="Start Camera Streaming",width=50,command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER,expand=True)

btn_screen=tk.Button(window,text="Start Screen Sharing",width=50,command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER,expand=True)

btn_audio=tk.Button(window,text="Start AUdio Stream",width=50,command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER,expand=True)

window.mainloop()
